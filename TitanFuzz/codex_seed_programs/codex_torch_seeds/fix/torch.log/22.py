'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log\ntorch.log(input, *, out=None)\n'
import torch
input_data = torch.Tensor([[1, 2], [3, 4]])
output = torch.log(input_data)
print(output)