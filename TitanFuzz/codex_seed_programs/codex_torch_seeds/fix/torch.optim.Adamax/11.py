'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adamax\ntorch.optim.Adamax(params, lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)\n'
import torch
import torch
x = torch.randn((1, 1), requires_grad=True)
y = torch.randn((1, 1), requires_grad=True)
optimizer = torch.optim.Adamax([x, y], lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)
optimizer.step()
optimizer.zero_grad()
state_dict = optimizer.state_dict()
optimizer.load_state_dict(state_dict)
param_groups = optimizer.param_groups