'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Threshold\ntorch.nn.Threshold(threshold, value, inplace=False)\n'
import torch
import numpy as np
import torch
input_data = torch.randn(1, 1, 4, 4)
threshold = torch.nn.Threshold(0.5, 0)
output = threshold(input_data)
print('input_data:\n', input_data)
print('output:\n', output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU\ntorch.nn.ReLU(inplace=False)\n'
import torch
import numpy as np
import torch
input_data = torch.randn(1, 1, 4, 4)
relu = torch.nn.ReLU()
output = relu(input_data)