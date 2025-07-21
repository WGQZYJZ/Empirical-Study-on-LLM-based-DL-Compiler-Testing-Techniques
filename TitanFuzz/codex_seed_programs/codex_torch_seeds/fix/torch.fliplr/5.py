'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fliplr\ntorch.fliplr(input)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input Data: ', input_data)
input_data = torch.fliplr(input_data)
print('Input Data after applying torch.fliplr: ', input_data)