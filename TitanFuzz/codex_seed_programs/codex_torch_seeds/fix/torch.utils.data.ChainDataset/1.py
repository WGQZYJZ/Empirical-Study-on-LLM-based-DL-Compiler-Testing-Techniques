'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.ChainDataset\ntorch.utils.data.ChainDataset(datasets)\n'
import torch
import torch
input_data = torch.rand(10)
input_data_new = torch.utils.data.ChainDataset([input_data])
print(input_data_new)