'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.parameter.UninitializedBuffer\ntorch.nn.parameter.UninitializedBuffer(requires_grad=False, device=None, dtype=None)\n'
import torch
a = torch.randn(3, 4)
print('a =\n', a)
b = torch.nn.parameter.UninitializedBuffer(requires_grad=False, device=None, dtype=None)
print('b =\n', b)