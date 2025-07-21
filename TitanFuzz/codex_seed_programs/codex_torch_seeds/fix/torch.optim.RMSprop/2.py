'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.RMSprop\ntorch.optim.RMSprop(params, lr=0.01, alpha=0.99, eps=1e-08, weight_decay=0, momentum=0, centered=False)\n'
import torch
x = torch.tensor(data=[2.0, 3.0], requires_grad=True)
print(x)
optimizer = torch.optim.RMSprop([x], lr=0.01)
for step in range(201):
    optimizer.zero_grad()
    y = (x * x)
    loss = ((y - 4) ** 2)