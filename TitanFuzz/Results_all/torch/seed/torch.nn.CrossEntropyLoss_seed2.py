x = torch.tensor([[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]])
y = torch.tensor([1, 0])
loss = torch.nn.CrossEntropyLoss()
output = loss(x, y)