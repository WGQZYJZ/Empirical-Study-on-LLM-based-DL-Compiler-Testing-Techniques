x = torch.tensor([[1.0, 1], [1, 2], [3, 4]], dtype=torch.float)
linear = torch.nn.LazyLinear(2, 2)
y = linear(x)