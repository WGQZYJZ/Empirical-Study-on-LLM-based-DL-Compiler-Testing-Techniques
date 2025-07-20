x = torch.randn(2, 3)
y = torch.logsumexp(x, dim=1, keepdim=True)