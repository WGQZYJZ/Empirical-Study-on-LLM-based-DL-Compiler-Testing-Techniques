x = torch.tensor([1.0], requires_grad=True)
y = torch.tensor([2.0], requires_grad=True)
optimizer = torch.optim.Adamax([x, y])
for i in range(10):
    optimizer.zero_grad()
    loss = ((x ** 2) + (y ** 2))
    loss.backward()
    optimizer.step()
    print(f'i: {i}, x: {x.item()}, y: {y.item()}, loss: {loss.item()}')