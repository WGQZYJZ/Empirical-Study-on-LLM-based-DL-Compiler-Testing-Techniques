'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adamax\ntorch.optim.Adamax(params, lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)\n'
import torch
x = torch.randn(1, requires_grad=True)
y = torch.randn(1, requires_grad=True)
optimizer = torch.optim.Adamax([x, y], lr=0.01)
for i in range(100):
    optimizer.zero_grad()
    loss = ((x ** 2) + (y ** 2))
    loss.backward()
    optimizer.step()
    print(i, x.item(), y.item())