a = torch.randn(3, 4)
b = torch.randn(4, 5)
c = torch.tensordot(a, b, dims=1)