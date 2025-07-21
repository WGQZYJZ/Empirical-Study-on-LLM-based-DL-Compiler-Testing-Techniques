"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.kaiming_normal_\ntorch.nn.init.kaiming_normal_(tensor, a=0, mode='fan_in', nonlinearity='leaky_relu')\n"
import torch
d = torch.randn(4, 4)
torch.nn.init.kaiming_normal_(d, a=0, mode='fan_in', nonlinearity='leaky_relu')
print(d)
print(d.grad)
torch.nn.init.kaiming_normal_(d, a=0, mode='fan_in', nonlinearity='leaky_relu')
print(d)
print(d.grad)