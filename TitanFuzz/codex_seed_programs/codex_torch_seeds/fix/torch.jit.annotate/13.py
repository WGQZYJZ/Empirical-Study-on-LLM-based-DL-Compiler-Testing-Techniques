'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.annotate\ntorch.jit.annotate(the_type, the_value)\n'
import torch
x = torch.rand(3, 3)
y = torch.rand(3, 3)
x_type = torch.jit.annotate(torch.Tensor, x)
y_type = torch.jit.annotate(torch.Tensor, y)
print(x_type)
print(y_type)
z = (x + y)
z_type = torch.jit.annotate(torch.Tensor, z)
print(z_type)