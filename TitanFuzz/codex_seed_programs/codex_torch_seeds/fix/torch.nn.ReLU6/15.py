'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU6\ntorch.nn.ReLU6(inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.randn(10, 20)
relu6 = nn.ReLU6()
output = relu6(input_data)
print(output)