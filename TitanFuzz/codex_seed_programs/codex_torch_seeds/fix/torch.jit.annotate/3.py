'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.annotate\ntorch.jit.annotate(the_type, the_value)\n'
import torch
x = torch.tensor(5.0, requires_grad=True)
x = torch.jit.annotate(torch.float32, x)
print('x:', x)
print('x.dtype:', x.dtype)