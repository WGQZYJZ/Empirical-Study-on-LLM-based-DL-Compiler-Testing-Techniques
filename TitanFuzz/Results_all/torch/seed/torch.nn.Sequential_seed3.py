x = torch.randn(100, 3)
y = torch.randn(100, 2)
net = torch.nn.Sequential(torch.nn.Linear(3, 10), torch.nn.ReLU(), torch.nn.Linear(10, 2))
loss_func = torch.nn.MSELoss()
optimizer = torch.optim.SGD(net.parameters(), lr=0.1)
for t in range(100):
    prediction = net(x)
    loss = loss_func(prediction, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()