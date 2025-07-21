'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.RAdam\ntorch.optim.RAdam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)\n'
import torch
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = torch.tensor([4.0, 5.0, 6.0], requires_grad=True)
z = torch.tensor([7.0, 8.0, 9.0], requires_grad=True)
optimizer = torch.optim.RAdam([x, y, z], lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)
print(optimizer.state_dict())