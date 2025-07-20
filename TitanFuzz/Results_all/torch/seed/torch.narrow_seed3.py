x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
out = torch.narrow(x, dim=1, start=1, length=2)