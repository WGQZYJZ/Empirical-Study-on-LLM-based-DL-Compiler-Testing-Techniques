'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveAvgPool1d\ntorch.nn.AdaptiveAvgPool1d(output_size)\n'
import torch
import numpy as np
if True:
    input_data = torch.arange(1, 11, dtype=torch.float32).reshape(1, 1, 10)
    print('input_data:', input_data)
    avg_pool1d = torch.nn.AdaptiveAvgPool1d(3)
    output_data = avg_pool1d(input_data)
    print('output_data:', output_data)