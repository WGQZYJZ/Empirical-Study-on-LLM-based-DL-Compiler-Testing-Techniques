'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.permute\ntorch.permute(input, dims)\n'
import torch
input_data = torch.tensor([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print('input_data: ', input_data)
print('input_data.shape: ', input_data.shape)
permute_data = torch.permute(input_data, (0, 2, 1))
print('permute_data: ', permute_data)
print('permute_data.shape: ', permute_data.shape)