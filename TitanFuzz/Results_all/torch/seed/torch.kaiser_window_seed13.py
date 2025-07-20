input_data = torch.randn(1, 1, 10)
output = torch.kaiser_window(10, periodic=True, beta=12.0)