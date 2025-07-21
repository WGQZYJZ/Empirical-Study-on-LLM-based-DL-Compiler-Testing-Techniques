'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardswish\ntorch.nn.Hardswish(inplace=False)\n'
import torch
import numpy as np
input_data = torch.randn(4, 4)
output = torch.nn.Hardswish()(input_data)
print(output)