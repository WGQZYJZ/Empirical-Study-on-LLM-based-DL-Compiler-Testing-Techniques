input = torch.randn(3, 4)
q = 0.5
dim = 0
keepdim = True
out = torch.quantile(input, q, dim, keepdim)