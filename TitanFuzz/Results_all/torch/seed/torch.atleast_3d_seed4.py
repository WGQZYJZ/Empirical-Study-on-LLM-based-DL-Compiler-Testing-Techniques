x = torch.rand(2, 3)
out = torch.atleast_3d(x)
out = torch.atleast_3d(x, x, x)
out = torch.atleast_3d(x, x, x, x)