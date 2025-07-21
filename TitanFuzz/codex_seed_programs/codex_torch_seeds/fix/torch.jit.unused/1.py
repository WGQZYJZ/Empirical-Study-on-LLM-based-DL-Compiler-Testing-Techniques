'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.unused\ntorch.jit.unused(fn)\n'
import torch
x = torch.rand(1, requires_grad=True)
torch.jit.unused(x)