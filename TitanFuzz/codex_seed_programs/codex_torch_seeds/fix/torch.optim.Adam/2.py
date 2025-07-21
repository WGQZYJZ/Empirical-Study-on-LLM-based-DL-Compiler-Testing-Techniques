'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adam\ntorch.optim.Adam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, amsgrad=False)\n'
import torch
data = torch.randn(2, 2)
target = torch.randn(2)
optimizer = torch.optim.Adam([data], lr=0.1)
optimizer.step()