'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adamax\ntorch.optim.Adamax(params, lr=0.002, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)\n'
import torch
x = torch.tensor([2.0], requires_grad=True)
y = torch.tensor([3.0])
optimizer = torch.optim.Adamax([x], lr=0.1)
for i in range(10):
    y_pred = (x * x)
    loss = ((y_pred - y) ** 2)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    print('Step {}, x = {}, loss = {}'.format(i, x.item(), loss.item()))