'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.RMSprop\ntorch.optim.RMSprop(params, lr=0.01, alpha=0.99, eps=1e-08, weight_decay=0, momentum=0, centered=False)\n'
import torch
x = torch.randn(3, requires_grad=True)
print('x: {}'.format(x))
optimizer = torch.optim.RMSprop([x], lr=0.01)
for i in range(3):
    optimizer.zero_grad()
    y = (x ** 2)
    loss = y.sum()
    loss.backward()
    optimizer.step()
    print('x: {}, loss: {}'.format(x, loss.item()))
print('Final x: {}'.format(x))