'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LeakyReLU\ntorch.nn.LeakyReLU(negative_slope=0.01, inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.Tensor([[(- 1), (- 2), (- 3)], [1, 2, 3]])
leaky_relu = nn.LeakyReLU(negative_slope=0.01, inplace=False)
output_data = leaky_relu(input_data)
print('Output data: \n', output_data)