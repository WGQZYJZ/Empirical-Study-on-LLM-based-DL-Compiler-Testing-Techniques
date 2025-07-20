input = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([[2, 3, 4], [5, 6, 7]])
torch.cross(input, other, dim=1)
input = torch.tensor([[1, 2, 3], [4, 5, 6]])
torch.cumprod(input, dim=1)
input