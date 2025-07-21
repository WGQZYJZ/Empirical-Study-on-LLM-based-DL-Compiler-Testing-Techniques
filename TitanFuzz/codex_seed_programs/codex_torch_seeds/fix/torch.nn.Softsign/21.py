'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softsign\ntorch.nn.Softsign()\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
x = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
softsign = nn.Softsign()
y = softsign(x)
print('input: ', x)
print('output: ', y)