'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softsign\ntorch.nn.Softsign()\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
input_data = torch.Tensor([[1, 2, 3, 4, 5]])
print('Input data: ', input_data)
softsign = nn.Softsign()
output_data = softsign(input_data)
print('Output data: ', output_data)