'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SELU\ntorch.nn.SELU(inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.tensor([(- 1), (- 0.5), 0, 0.5, 1], dtype=torch.float)
selu = nn.SELU(inplace=False)
output = selu(input_data)
print(output)