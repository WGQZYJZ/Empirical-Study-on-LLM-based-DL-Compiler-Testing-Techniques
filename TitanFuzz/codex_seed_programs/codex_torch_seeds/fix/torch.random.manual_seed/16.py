'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.manual_seed\ntorch.random.manual_seed(seed)\n'
import torch
x = torch.rand(2, 3, requires_grad=True)
print('x: ', x)
torch.random.manual_seed(1)
x = torch.rand(2, 3, requires_grad=True)
print('x: ', x)
torch.random.manual_seed(1)
x = torch.rand(2, 3, requires_grad=True)
print('x: ', x)