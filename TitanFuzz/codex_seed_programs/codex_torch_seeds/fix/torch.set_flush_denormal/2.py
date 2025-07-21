'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_flush_denormal\ntorch.set_flush_denormal(mode)\n'
import torch
import sys
x = torch.randn(3, 3)
y = torch.randn(3, 3)
torch.set_flush_denormal(True)
print(x)
print(y)
print(sys.float_info.epsilon)
print(sys.float_info.min)
print(sys.float_info.max)
print((x + y))