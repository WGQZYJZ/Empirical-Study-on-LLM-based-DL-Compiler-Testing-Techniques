'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.NAdam\ntorch.optim.NAdam(params, lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, momentum_decay=0.004)\n'
import torch
import numpy as np
x = torch.randn(2, 3)
y = torch.randn(2, 3)
import torch
import numpy as np
x = torch.randn(2, 3)
y = torch.randn(2, 3)
x = torch.randn(2, 3)
y = torch.randn(2, 3)
optimizer = torch.optim.NAdam([x, y], lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, momentum_decay=0.004)
print(optimizer.param_groups[0]['params'])
print(optimizer.param_groups[0]['lr'])
print(optimizer.param_groups[0]['betas'])
print(optimizer.param_groups[0]['eps'])