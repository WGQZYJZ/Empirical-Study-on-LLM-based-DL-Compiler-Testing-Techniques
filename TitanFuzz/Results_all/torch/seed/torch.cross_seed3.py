a = torch.tensor([[1, 2, 3], [4, 5, 6]])
b = torch.tensor([[1, 1, 1], [2, 2, 2]])
c = torch.cross(a, b)
c = torch.cross(a, b, dim=1)