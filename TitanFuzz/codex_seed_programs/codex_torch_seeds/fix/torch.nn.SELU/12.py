'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SELU\ntorch.nn.SELU(inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.Tensor([[1, 2, 3], [4, 5, 6]])
selu = nn.SELU(inplace=False)
output_data = selu(input_data)
print(output_data)