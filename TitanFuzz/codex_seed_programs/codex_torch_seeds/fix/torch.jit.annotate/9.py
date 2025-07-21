'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.annotate\ntorch.jit.annotate(the_type, the_value)\n'
import torch
x = torch.rand(1, 3, 224, 224)
x = torch.jit.annotate(torch.Tensor, x)
print(x)