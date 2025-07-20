A = torch.randn(3, 2)
b = torch.randn(3)
(x, _) = torch.lstsq(b, A)