'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.annotate\ntorch.jit.annotate(the_type, the_value)\n'
import torch
x = torch.rand(4, 4)
y = torch.rand(4, 4)
z = torch.jit.annotate(torch.Tensor, None)
for i in range(10):
    z = (x + y)
    print(z)