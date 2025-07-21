'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU6\ntorch.nn.ReLU6(inplace=False)\n'
import torch
import torch.nn as nn
import numpy as np
input_data = np.array([(- 1), 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
input_data = torch.from_numpy(input_data)
relu6 = nn.ReLU6()
output = relu6(input_data)
print(output)