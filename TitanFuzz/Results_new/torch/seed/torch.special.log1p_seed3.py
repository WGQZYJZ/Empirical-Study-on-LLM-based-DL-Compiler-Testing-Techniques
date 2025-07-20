x = torch.rand(1, requires_grad=True)
y = torch.special.log1p(x)
y.backward()