a = torch.rand(3, 4)
b = torch.rand(3, 4)
c = torch.column_stack((a, b))
d = torch.column_stack((a, b, a))