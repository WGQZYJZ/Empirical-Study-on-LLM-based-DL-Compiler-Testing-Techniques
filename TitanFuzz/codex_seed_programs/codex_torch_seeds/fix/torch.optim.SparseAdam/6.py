'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.SparseAdam\ntorch.optim.SparseAdam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08)\n'
import torch
import torch.optim as optim
input_data = torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
target_data = torch.tensor([10.0, 20.0, 30.0])
weight_data = torch.tensor([0.5, 0.5])
optimizer = optim.SparseAdam(weight_data, lr=0.001)
print('Default parameter values:')
print('lr: ', optimizer.defaults['lr'])
print('betas: ', optimizer.defaults['betas'])