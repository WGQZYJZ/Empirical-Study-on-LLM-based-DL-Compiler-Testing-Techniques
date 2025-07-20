x = torch.tensor([1.0])
y = torch.tensor([2.0])
loss = torch.nn.MSELoss()
loss = loss(x, y)