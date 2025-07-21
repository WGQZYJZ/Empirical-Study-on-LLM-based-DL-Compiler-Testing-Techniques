'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logit\ntorch.special.logit(input, eps=None, *, out=None)\n'
import torch
input_data = torch.randn((2, 3))
print(input_data)
logit_data = torch.special.logit(input_data)
print(logit_data)
print(torch.sigmoid(logit_data))