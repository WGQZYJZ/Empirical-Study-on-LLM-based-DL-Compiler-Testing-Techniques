'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.RMSprop\ntorch.optim.RMSprop(params, lr=0.01, alpha=0.99, eps=1e-08, weight_decay=0, momentum=0, centered=False)\n'
import torch
params = torch.tensor([1.0, 0.0], requires_grad=True)
print(params)
optimizer = torch.optim.RMSprop([params], lr=0.01, alpha=0.99, eps=1e-08, weight_decay=0, momentum=0, centered=False)
print(optimizer)
optimizer.zero_grad()
loss = ((params[0] ** 2) + (params[1] ** 2))
loss.backward()
optimizer.step()
print(params)