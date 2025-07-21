input_data = torch.arange(0, 10, dtype=torch.float)
window = torch.hann_window(10, periodic=True, dtype=torch.float)