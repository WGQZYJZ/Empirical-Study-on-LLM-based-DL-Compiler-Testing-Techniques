a = torch.randn(3, 3)
a = ((a * 3) / (a - 1))
(q, r) = torch.geqrf(a)