"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.kaiming_normal_\ntorch.nn.init.kaiming_normal_(tensor, a=0, mode='fan_in', nonlinearity='leaky_relu')\n"
import torch
import torch
input_tensor = torch.rand(2, 3, 5, 5)
torch.nn.init.kaiming_normal_(input_tensor, a=0, mode='fan_in', nonlinearity='leaky_relu')
print(input_tensor)
"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.kaiming_uniform_\ntorch.nn.init.kaiming_uniform_(tensor, a=0, mode='fan_in', nonlinearity='leaky_relu')\n"
import torch
import torch
input_tensor = torch.rand(2, 3, 5, 5)