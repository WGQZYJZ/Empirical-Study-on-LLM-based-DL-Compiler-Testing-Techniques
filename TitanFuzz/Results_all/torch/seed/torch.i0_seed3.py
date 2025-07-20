x = torch.randn(1, requires_grad=True)
y = torch.i0(x)
y.backward()