x = torch.tensor(data=[2.0], requires_grad=True)
y = (x ** 2)
optimizer = torch.optim.RMSprop(params=[x], lr=0.01, alpha=0.99, eps=1e-08, weight_decay=0, momentum=0, centered=False)
for epoch in range(1000):
    y = (x ** 2)
    loss = y.sum()
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if ((epoch % 100) == 0):
        print('epoch {}, x = {}, loss = {}'.format(epoch, x.item(), loss.item()))