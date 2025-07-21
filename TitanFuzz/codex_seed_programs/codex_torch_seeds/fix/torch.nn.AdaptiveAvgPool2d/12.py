'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool2d\ntorch.nn.AdaptiveAvgPool2d(output_size)\n'
import torch
import torch.nn as nn
import numpy as np
input_data = np.random.randn(2, 3, 5, 5)
input_data = torch.from_numpy(input_data)
output_size = (2, 2)
avg_pool = nn.AdaptiveAvgPool2d(output_size)
output = avg_pool(input_data)
print(output)