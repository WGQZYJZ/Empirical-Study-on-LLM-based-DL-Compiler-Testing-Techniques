x = torch.tensor([[1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 1.0, 1.0]], requires_grad=True)
y = torch.tensor([[1.0, 0.0, 1.0, 0.0, 1.0], [0.0, 1.0, 1.0, 0.0, 1.0], [1.0, 0.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 0.0, 0.0], [1.0, 0.0, 1.0, 1.0, 0.0]], requires_grad=True)
loss = torch.nn.BCEWithLogitsLoss()
output = loss(x, y)
output.backward()