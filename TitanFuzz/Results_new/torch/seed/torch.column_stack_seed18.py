a = torch.rand(2, 3)
b = torch.rand(2, 3)
c = torch.column_stack((a, b))
d = torch.cat((a, b), dim=1)