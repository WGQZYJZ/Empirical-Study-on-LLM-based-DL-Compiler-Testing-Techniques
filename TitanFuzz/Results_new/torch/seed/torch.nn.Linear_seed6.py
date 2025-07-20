X = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
linear = torch.nn.Linear(3, 1)
y = linear(X)