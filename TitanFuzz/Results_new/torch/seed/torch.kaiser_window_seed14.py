input_data = torch.arange(0, 10, 1)
window = torch.kaiser_window(10, periodic=True, beta=12.0, dtype=torch.float)