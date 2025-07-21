"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.kaiming_uniform_\ntorch.nn.init.kaiming_uniform_(tensor, a=0, mode='fan_in', nonlinearity='leaky_relu')\n"
import torch
import torch.nn as nn
input_data = torch.rand(3, 3)
nn.init.kaiming_uniform_(input_data, a=0, mode='fan_in', nonlinearity='leaky_relu')
print(input_data)
"\nTask 4: Call the API torch.nn.init.kaiming_normal_\ntorch.nn.init.kaiming_normal_(tensor, a=0, mode='fan_in', nonlinearity='leaky_relu')\n"
nn.init.kaiming_normal_(input_data, a=0, mode='fan_in', nonlinearity='leaky_relu')
print(input_data)