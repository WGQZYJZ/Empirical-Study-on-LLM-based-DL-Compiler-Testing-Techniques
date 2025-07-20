A = torch.rand(3, 3)
b = torch.rand(3, 1)
x = torch.lstsq(b, A)