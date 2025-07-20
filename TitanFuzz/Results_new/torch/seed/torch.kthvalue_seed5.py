input = torch.randn(3, 4)
k = 2
dim = 0
keepdim = False
out = torch.kthvalue(input, k, dim, keepdim)