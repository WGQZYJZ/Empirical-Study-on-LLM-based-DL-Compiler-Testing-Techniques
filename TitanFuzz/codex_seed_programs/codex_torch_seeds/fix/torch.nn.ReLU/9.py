'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU\ntorch.nn.ReLU(inplace=False)\n'
import torch
import numpy as np
input_data = np.random.randn(100, 100)
input_data = torch.Tensor(input_data)
relu_layer = torch.nn.ReLU(inplace=False)
output = relu_layer(input_data)
print(output)