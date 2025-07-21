'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lt\ntorch.lt(input, other, *, out=None)\n'
import torch
input_data = torch.Tensor([[1, 2], [3, 4]])
output_data = torch.lt(input_data, torch.Tensor([[1, 1], [4, 4]]))
print(output_data)