x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x_rot90 = torch.rot90(x, 1, dims=(0, 1))