'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logit\ntorch.logit(input, eps=None, *, out=None)\n'
import torch
input_data = torch.rand(3, 3)
print(input_data)
output_data = torch.logit(input_data)
print(output_data)