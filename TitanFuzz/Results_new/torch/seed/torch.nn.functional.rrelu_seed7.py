x = torch.randn(1, 2, 3, requires_grad=True)
y = torch.nn.functional.rrelu(x)
y.sum().backward()