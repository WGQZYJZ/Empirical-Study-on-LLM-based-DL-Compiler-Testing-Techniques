'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.dropout\ntorch.nn.functional.dropout(input, p=0.5, training=True, inplace=False)\n'
import torch
import numpy as np
import torch
input_data = torch.rand(100, 1000)
output_data = torch.nn.functional.dropout(input_data, p=0.5, training=True, inplace=False)
print(output_data)