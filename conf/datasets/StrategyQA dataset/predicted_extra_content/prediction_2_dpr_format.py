import json
import pandas as pd
import json
import spacy
nlp = spacy.load("en_core_web_lg")

from  evaluation.single_label_metric_evaluators_from_json import  list_to_unique_list
def load_data(path):
    with open(path) as json_file:
        data = json.load(json_file)
        return data


def remove_duplicate_by_lemma(token_list):
    lemma_list = []
    new_tokens_list  = []
    for token in token_list:
        if len(token)>0:
            tok_lemma = nlp(token)[0].lemma_
            if tok_lemma not in lemma_list:
                lemma_list.append(tok_lemma)
                new_tokens_list.append(token)

    return new_tokens_list

def remove_duplicate_token_in_question(token_list,question):
    question_tokens  = question.split()
    new_tokens_list = []
    for token in token_list:
        if token not in question_tokens:
            new_tokens_list.append(token)
    return new_tokens_list

def combine_clean(tokens,question):
    tokens = remove_duplicate_by_lemma(tokens)
    tokens = remove_duplicate_token_in_question(tokens,question)
    return tokens
path = '/Users/uri/Documents/Uri/school/Thesis/Implicit/thesis/Experiments/Extract_strategy_from_SQA_decomp/Strategy_extraction/results/single_label_31_07/extra_content_description_single_label_top20_t5_large/eval_output_extra_content_single.json'
data = pd.DataFrame(load_data(path))[['qid','question','top_tokens_by_lm']].drop_duplicates(subset='qid')

REMOVE_TOKENS_INCLUDED_IN_QUESTION = True
REMOVE_LAST_TOKEN_IF_DUPLICATED = True
data['new tokens'] = data.apply(lambda x: combine_clean(x['top_tokens_by_lm'], x['question']), axis=1)






datatype = 'dev'
path = '/Users/uri/Documents/Uri/school/Thesis/Implicit/thesis/DPR/conf/datasets/StrategyQA dataset/gold/strategyQA_'+datatype+'.json'
with open(path) as json_file:
    dpr_format_data = json.load(json_file)


path = '/Users/uri/Documents/Uri/school/Thesis/Implicit/thesis/Experiments/Extract_strategy_from_SQA_decomp/Strategy_extraction/seq2seq_strategy_extractor/data/strategyqa_data_with_labels/' + datatype + '.json'
with open(path) as json_file:
    labeled_data = json.load(json_file)

for i,sample_in_dpr_data in enumerate(dpr_format_data):
    question_changed = False
    question = sample_in_dpr_data['question']
    for sample_in_labeld_data in labeled_data:
        if sample_in_labeld_data['question'] == question:
            if len(data[data['qid']==sample_in_labeld_data['qid']])>0:
                extra_content = ' ; '.join(data[data['qid']==sample_in_labeld_data['qid']]['new tokens'].item())
                sample_in_dpr_data['question'] = '{} {}'.format(question,extra_content)
                sample_in_dpr_data['qid'] = sample_in_labeld_data['qid']
                question_changed = True
            break

    if not question_changed:
        sample_in_dpr_data['qid'] = sample_in_labeld_data['qid']
        print('i')

output_file = 'strategyQA_'+datatype+'_for_mapping.json'
with open(output_file,"w") as fd:
        json.dump(dpr_format_data, fd)


dpr_format_data_no_qid = [{k: v for k, v in d.items() if k != 'qid'} for d in dpr_format_data]

output_file = 'strategyQA_'+datatype+'.json'
with open(output_file,"w") as fd:
        json.dump(dpr_format_data_no_qid, fd)



