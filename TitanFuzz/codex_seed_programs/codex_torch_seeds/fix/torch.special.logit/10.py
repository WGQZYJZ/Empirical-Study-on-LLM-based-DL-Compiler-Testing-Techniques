'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logit\ntorch.special.logit(input, eps=None, *, out=None)\n'
import torch
input_data = torch.rand(3, 5)
output = torch.special.logit(input_data)
print(output)