"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.kaiming_normal_\ntorch.nn.init.kaiming_normal_(tensor, a=0, mode='fan_in', nonlinearity='leaky_relu')\n"
import torch
import numpy as np
input_data = np.random.randn(5, 3)
input_data = torch.tensor(input_data, dtype=torch.float)
print('input_data:', input_data)
torch.nn.init.kaiming_normal_(input_data, a=0, mode='fan_in', nonlinearity='leaky_relu')
print('input_data:', input_data)