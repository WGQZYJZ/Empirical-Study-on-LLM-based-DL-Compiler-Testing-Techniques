'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.logit\ntorch.special.logit(input, eps=None, *, out=None)\n'
import torch
input = torch.randn((2, 3), dtype=torch.float32, requires_grad=True)
output = torch.special.logit(input, eps=1e-12)
print(output)
print(output.grad_fn)