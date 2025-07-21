'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU6\ntorch.nn.ReLU6(inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
relu6 = nn.ReLU6()
output = relu6(input_data)
print('Input: ', input_data)
print('Output: ', output)