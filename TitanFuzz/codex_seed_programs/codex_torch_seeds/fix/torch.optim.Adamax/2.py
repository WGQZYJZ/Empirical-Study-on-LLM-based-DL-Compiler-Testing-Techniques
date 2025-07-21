'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adamax\ntorch.optim.Adamax(params, lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)\n'
import torch
x = torch.randn(1, requires_grad=True)
y = torch.randn(1, requires_grad=True)
optimizer = torch.optim.Adamax([x, y], lr=0.1)
for i in range(10):
    optimizer.zero_grad()
    z = ((x ** 2) + (y ** 2))
    z.backward()
    print(x.grad, y.grad)
    optimizer.step()