x = torch.randn(3, 3)
y = torch.randn(3, 3)
torch._assert((x.size() == y.size()), 'x and y must have the same size')