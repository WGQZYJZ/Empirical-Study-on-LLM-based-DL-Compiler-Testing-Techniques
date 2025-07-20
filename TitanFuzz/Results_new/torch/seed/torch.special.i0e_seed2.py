x = torch.rand(10)
y = torch.special.i0e(x)
y = torch.special.i0e(x, out=torch.empty(10))