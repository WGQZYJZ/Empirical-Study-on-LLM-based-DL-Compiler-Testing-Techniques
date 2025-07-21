'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU6\ntorch.nn.ReLU6(inplace=False)\n'
import torch
x = torch.randn(3, 5)
print(x)
relu6 = torch.nn.ReLU6()
print(relu6(x))
print(torch.clamp(x, min=0, max=6))