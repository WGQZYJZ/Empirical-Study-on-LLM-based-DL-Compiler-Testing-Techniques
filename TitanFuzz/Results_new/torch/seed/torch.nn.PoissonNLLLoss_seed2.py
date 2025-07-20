input = torch.randn(1, 3, 3, 3, requires_grad=True)
target = torch.randn(1, 3, 3, 3)
loss = torch.nn.PoissonNLLLoss()
output = loss(input, target)