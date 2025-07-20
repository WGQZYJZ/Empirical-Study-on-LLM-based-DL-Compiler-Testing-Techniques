data = torch.randn(5, 3)
label = torch.tensor([1, 0, 2, 1, 1])
loss = torch.nn.CrossEntropyLoss()
output = loss(data, label)