'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.NAdam\ntorch.optim.NAdam(params, lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, momentum_decay=0.004)\n'
import torch
from torch.optim import NAdam
x = torch.rand(20, requires_grad=True)
optimizer = NAdam([x], lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, momentum_decay=0.004)
print(optimizer)