input_data_1 = torch.rand(size=(3, 3))
input_data_2 = torch.rand(size=(3, 3))
input_data_3 = torch.rand(size=(3, 3))
dataset = torch.utils.data.ConcatDataset([input_data_1, input_data_2, input_data_3])