'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout2d\ntorch.nn.Dropout2d(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
import numpy as np
input_data = np.random.random((2, 3, 4, 4))
input_data = torch.tensor(input_data, dtype=torch.float32)
print('input_data: ', input_data)
dropout2d = nn.Dropout2d(p=0.5, inplace=False)
output_data = dropout2d(input_data)
print('output_data: ', output_data)