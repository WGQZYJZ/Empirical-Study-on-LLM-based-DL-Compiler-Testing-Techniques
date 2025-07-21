'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu6\ntorch.nn.functional.relu6(input, inplace=False)\n'
import torch
import numpy as np
import torch
input_data = np.random.randn(2, 3)
input_data = torch.tensor(input_data)
print(input_data)
output = torch.nn.functional.relu6(input_data)
print(output)
print('input: ', input_data)
print('output: ', output)