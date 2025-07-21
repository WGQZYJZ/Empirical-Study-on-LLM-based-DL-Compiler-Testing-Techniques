'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.NAdam\ntorch.optim.NAdam(params, lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, momentum_decay=0.004)\n'
import torch
x = torch.randn(1, requires_grad=True)
y = torch.randn(1, requires_grad=True)
optimizer = torch.optim.NAdam([x, y], lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, momentum_decay=0.004)
print(optimizer)
print(optimizer.param_groups[0]['betas'])
print(optimizer.param_groups[0]['momentum_decay'])
print(optimizer.param_groups[0]['eps'])
print(optimizer.defaults)