a = torch.randn(3, 4, 5)
b = torch.randn(4, 5, 6)
c = torch.tensordot(a, b, dims=2)