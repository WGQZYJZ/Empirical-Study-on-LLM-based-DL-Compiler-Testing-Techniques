x = torch.tensor([[[1, 1, 1], [1, 1, 1]], [[2, 2, 2], [2, 2, 2]], [[3, 3, 3], [3, 3, 3]]])
x_flatten = torch.flatten(x, start_dim=1, end_dim=(- 1))