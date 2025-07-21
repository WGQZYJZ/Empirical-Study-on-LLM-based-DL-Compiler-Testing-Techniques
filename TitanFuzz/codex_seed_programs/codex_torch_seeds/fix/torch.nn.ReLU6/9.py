'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU6\ntorch.nn.ReLU6(inplace=False)\n'
import torch
x = torch.randn(4, 4)
print(x)
relu6 = torch.nn.ReLU6()
print(relu6(x))