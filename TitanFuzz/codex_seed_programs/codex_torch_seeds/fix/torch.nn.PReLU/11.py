'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PReLU\ntorch.nn.PReLU(num_parameters=1, init=0.25, device=None, dtype=None)\n'
import torch
x = torch.randn(1, 4)
print(x)
prelu = torch.nn.PReLU(num_parameters=1, init=0.25)
print(prelu)
y = prelu(x)
print(y)
prelu = torch.nn.PReLU(num_parameters=4, init=0.25)
print(prelu)
y = prelu(x)
print(y)