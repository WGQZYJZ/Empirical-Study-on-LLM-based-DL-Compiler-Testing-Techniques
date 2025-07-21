"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pad\ntorch.nn.functional.pad(input, pad, mode='constant', value=0)\n"
import torch
import torch
input = torch.tensor([[[1, 2, 3], [4, 5, 6]]])
print('input shape: ', input.shape)
output = torch.nn.functional.pad(input, pad=(0, 1, 0, 1), mode='constant', value=0)
print('output shape: ', output.shape)
print('output: ', output)