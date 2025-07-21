'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_dtype\ntorch.set_default_dtype(d)\n'
import torch as t
x = t.randn(1, 2, 3, 4, requires_grad=True)
print(x)
print(x.dtype)
t.set_default_dtype(t.float64)
x = t.randn(1, 2, 3, 4, requires_grad=True)
print(x)
print(x.dtype)