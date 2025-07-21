'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.isinstance\ntorch.jit.isinstance(obj, target_type)\n'
import torch
a = torch.randn(1, 2, 3, 4)
b = torch.randn(1, 2, 3, 4)
c = torch.randn(1, 2, 3, 4)
if (torch.jit.isinstance(a, torch.Tensor) and torch.jit.isinstance(b, torch.Tensor) and torch.jit.isinstance(c, torch.Tensor)):
    print('a, b, c are all tensor')
else:
    print('a, b, c are not all tensor')