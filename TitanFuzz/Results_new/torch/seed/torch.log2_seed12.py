x = torch.randn(1, requires_grad=True)
y = torch.log2(x)
y.backward()