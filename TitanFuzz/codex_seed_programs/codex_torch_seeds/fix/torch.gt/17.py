'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.gt\ntorch.gt(input, other, *, out=None)\n'
import torch
input_data_1 = torch.randn(3, 3)
input_data_2 = torch.randn(3, 3)
print(torch.gt(input_data_1, input_data_2))