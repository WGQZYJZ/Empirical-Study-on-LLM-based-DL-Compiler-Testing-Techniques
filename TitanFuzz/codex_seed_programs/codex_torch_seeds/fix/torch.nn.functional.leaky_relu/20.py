'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.leaky_relu\ntorch.nn.functional.leaky_relu(input, negative_slope=0.01, inplace=False)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
input_data = np.random.randn(1, 3, 5, 5)
input_data = torch.FloatTensor(input_data)
output_data = F.leaky_relu(input_data, 0.01)
print(input_data)
print(output_data)