input = torch.randn((1, 3, 3))
dim = 1
unbiased = True
keepdim = True
out = torch.var_mean(input, dim, unbiased, keepdim)