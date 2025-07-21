'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.trace\n'
import torch
x = torch.rand(2, 3)
traced_script_module = torch.jit.trace(torch.sum, x)
print(traced_script_module(x))