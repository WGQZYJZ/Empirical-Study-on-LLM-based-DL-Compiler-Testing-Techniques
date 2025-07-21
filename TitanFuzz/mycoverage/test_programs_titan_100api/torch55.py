import torch
x = torch.tensor(1.0, requires_grad=True)
optimizer = torch.optim.Adamax([x], lr=0.1)
for epoch in range(10):
    optimizer.zero_grad()
    y = (x ** 2)
    loss = y.sum()
    loss.backward()
    optimizer.step()
    print('Epoch {}, x: {}, loss: {}'.format(epoch, x.item(), loss.item()))