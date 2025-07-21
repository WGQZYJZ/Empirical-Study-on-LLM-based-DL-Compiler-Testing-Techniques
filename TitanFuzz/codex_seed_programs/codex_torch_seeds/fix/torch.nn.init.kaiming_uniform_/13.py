"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.kaiming_uniform_\ntorch.nn.init.kaiming_uniform_(tensor, a=0, mode='fan_in', nonlinearity='leaky_relu')\n"
import torch
x = torch.zeros(5, 5)
print(x)
torch.nn.init.kaiming_uniform_(x, a=0, mode='fan_in', nonlinearity='leaky_relu')
print(x)