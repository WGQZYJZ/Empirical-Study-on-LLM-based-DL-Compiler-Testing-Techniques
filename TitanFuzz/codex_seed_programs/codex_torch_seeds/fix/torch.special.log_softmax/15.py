'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.log_softmax\ntorch.special.log_softmax(input, dim, *, dtype=None)\n'
import torch
input = torch.randn(2, 3, requires_grad=True)
output = torch.special.log_softmax(input, dim=0)
print(output)