y = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
cum_trapz = torch.cumulative_trapezoid(y, x)