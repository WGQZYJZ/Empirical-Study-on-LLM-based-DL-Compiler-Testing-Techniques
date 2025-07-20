input_data_1 = torch.randn(100, 2)
input_data_2 = torch.randn(100, 2)
input_data_3 = torch.randn(100, 2)
datasets = [input_data_1, input_data_2, input_data_3]
concat_datasets = torch.utils.data.ConcatDataset(datasets)