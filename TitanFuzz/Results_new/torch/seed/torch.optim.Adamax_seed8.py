x = torch.randn(1, requires_grad=True)
y = torch.randn(1, requires_grad=True)
optimizer = torch.optim.Adamax([x, y], lr=0.01)
for i in range(100):
    optimizer.zero_grad()
    loss = ((x ** 2) + (y ** 2))
    loss.backward()
    optimizer.step()
    print(i, x.item(), y.item())