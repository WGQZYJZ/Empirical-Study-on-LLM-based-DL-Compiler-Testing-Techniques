'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.RAdam\ntorch.optim.RAdam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)\n'
import torch
import torch.optim as optim
x = torch.randn(1, requires_grad=True)
optimizer = optim.RAdam([x], lr=0.001)
for epoch in range(1000):
    optimizer.zero_grad()
    loss = (x ** 2)
    loss.backward()
    optimizer.step()
    print(x)