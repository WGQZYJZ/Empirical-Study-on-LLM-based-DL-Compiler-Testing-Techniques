x = torch.randn(3, requires_grad=True)
y = torch.tensor([1.0, (- 1.0), 1.0], dtype=torch.float)
loss = torch.nn.SoftMarginLoss()
output = loss(x, y)