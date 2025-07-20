input = torch.randn(3, 5, requires_grad=True)
target = torch.randn(3, 5)
loss = torch.nn.KLDivLoss()
output = loss(input, target)