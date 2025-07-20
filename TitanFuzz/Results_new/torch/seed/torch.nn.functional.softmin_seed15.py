x = torch.randn(3, requires_grad=True)
y = torch.nn.functional.softmin(x, dim=0)
z = torch.nn.Softmin(dim=0)