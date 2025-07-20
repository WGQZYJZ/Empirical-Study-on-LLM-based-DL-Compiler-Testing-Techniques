input = torch.randn(3, 4)
dim = 1
keepdim = False
out = torch.logsumexp(input, dim, keepdim, out=None)