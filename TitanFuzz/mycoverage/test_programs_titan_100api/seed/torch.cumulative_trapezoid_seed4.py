y = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=torch.float32)
integral_y = torch.cumulative_trapezoid(y)