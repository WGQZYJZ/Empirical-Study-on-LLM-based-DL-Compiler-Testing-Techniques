a = torch.rand(2, 3)
b = torch.rand(2, 3)
c = torch.true_divide(a, b)
c = torch.true_divide(a, b, out=c)