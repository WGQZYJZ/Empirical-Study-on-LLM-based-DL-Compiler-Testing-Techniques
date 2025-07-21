'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LeakyReLU\ntorch.nn.LeakyReLU(negative_slope=0.01, inplace=False)\n'
import torch
import numpy as np
input_data = torch.tensor([(- 1), 0, 1], dtype=torch.float)
relu_layer = torch.nn.LeakyReLU(negative_slope=0.01, inplace=False)
output_data = relu_layer(input_data)
print(output_data)