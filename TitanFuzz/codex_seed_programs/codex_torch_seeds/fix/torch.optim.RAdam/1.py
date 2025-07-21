'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.RAdam\ntorch.optim.RAdam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)\n'
import torch
import torch.optim as optim
import torch
x = torch.randn(1, requires_grad=True)
optimizer = optim.RAdam([x], lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)
optimizer.step()
print(x)