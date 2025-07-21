'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adamax\ntorch.optim.Adamax(params, lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)\n'
import torch
x = torch.tensor(1.0, requires_grad=True)
print(x)
optimizer = torch.optim.Adamax([x], lr=0.1)
print(optimizer)
for epoch in range(10):
    optimizer.zero_grad()
    y = (x ** 2)
    loss = y.sum()
    loss.backward()
    optimizer.step()
    print('Epoch {}, x: {}, loss: {}'.format(epoch, x.item(), loss.item()))