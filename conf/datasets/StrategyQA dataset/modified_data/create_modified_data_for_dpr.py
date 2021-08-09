import json

datatype = 'train'
path = '../strategyQA_' + datatype + '.json'
with open(path) as json_file:
    data = json.load(json_file)


path = '/Users/uri/Documents/Uri/school/Thesis/Implicit/thesis/Experiments/Extract_strategy_from_SQA_decomp/Strategy_extraction/seq2seq_strategy_extractor/data/strategyqa_data_with_labels/' + datatype + '.json'
with open(path) as json_file:
    labeled_data = json.load(json_file)

for i,sample_in_dpr_data in enumerate(data):
    question_changed = False
    question = sample_in_dpr_data['question']
    for sample_in_labeld_data in labeled_data:
        if sample_in_labeld_data['question'] == question:
            extra_content = sample_in_labeld_data['extra_content_outer']
            sample_in_dpr_data['question'] = '{} {}'.format(question,extra_content)
            question_changed = True
            break

    if not question_changed:
        print('i')


output_file = 'gold/strategyQA_'+datatype+'.json'
with open(output_file,"w") as fd:
        json.dump(data, fd)