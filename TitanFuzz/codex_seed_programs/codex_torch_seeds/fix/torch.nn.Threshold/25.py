'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Threshold\ntorch.nn.Threshold(threshold, value, inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.randn(3, 3)
threshold_obj = nn.Threshold(0.5, 0)
output = threshold_obj(input_data)
print('Input data: \n{}'.format(input_data))
print('Output data: \n{}'.format(output))