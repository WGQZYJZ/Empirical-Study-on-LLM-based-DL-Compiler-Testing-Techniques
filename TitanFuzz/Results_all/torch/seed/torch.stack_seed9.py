a = torch.rand(2, 3)
b = torch.rand(2, 3)
c = torch.rand(2, 3)
d = torch.stack([a, b, c], dim=0)
d = torch.stack([a, b, c], dim=1)
d = torch.stack([a, b, c], dim=2)