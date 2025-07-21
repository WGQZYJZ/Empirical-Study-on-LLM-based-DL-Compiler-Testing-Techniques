'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.annotate\ntorch.jit.annotate(the_type, the_value)\n'
import torch
x = torch.tensor(1.0)
y = torch.tensor(2.0)
z = torch.jit.annotate(torch.Tensor, (x + y))
print(z)