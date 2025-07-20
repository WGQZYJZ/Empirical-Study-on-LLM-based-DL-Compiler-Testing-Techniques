input_data = torch.randn(5, 5)
output_data = torch.kaiser_window(5, periodic=True, beta=12.0)