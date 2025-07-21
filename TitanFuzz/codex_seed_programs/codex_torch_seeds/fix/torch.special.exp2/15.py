'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.exp2\ntorch.special.exp2(input, *, out=None)\n'
import torch
if True:
    a = torch.rand(2, 3, requires_grad=True)
    print(a)
    print(torch.special.exp2(a))