x = torch.randn((2, 4))
q = torch.quantile(x, 0.5, dim=1, keepdim=True)
y = torch.quantile(x, 0.5, dim=1, keepdim=False)