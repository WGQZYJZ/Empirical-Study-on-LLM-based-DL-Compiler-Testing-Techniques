'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.ConcatDataset\ntorch.utils.data.ConcatDataset(datasets)\n'
import torch
import torch
input_data_1 = torch.rand(5, 3)
input_data_2 = torch.rand(5, 3)
input_data_3 = torch.rand(5, 3)
dataset = torch.utils.data.ConcatDataset([input_data_1, input_data_2, input_data_3])