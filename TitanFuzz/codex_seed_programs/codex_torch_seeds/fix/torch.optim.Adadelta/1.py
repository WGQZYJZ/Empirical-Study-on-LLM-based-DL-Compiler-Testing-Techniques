'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adadelta\ntorch.optim.Adadelta(params, lr=1.0, rho=0.9, eps=1e-06, weight_decay=0)\n'
import torch
import torch.optim as optim
import torch
import torch.optim as optim
input_data = torch.tensor([[1.0, 2.0], [3.0, 4.0]], requires_grad=True)
optimizer = optim.Adadelta(params=[input_data], lr=1.0, rho=0.9, eps=1e-06, weight_decay=0)
print('Parameter Group:')
print(optimizer.param_groups)
print('Parameter Group:')
print(optimizer.param_groups)
print('Parameter Group:')
print(optimizer.param_groups)
print('Parameter Group:')
print(optimizer.param_groups)
print('Parameter Group:')
print(optimizer.param_groups)