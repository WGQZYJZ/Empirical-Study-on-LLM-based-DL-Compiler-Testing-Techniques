input_data = torch.arange(1, 11, dtype=torch.float)
window_data = torch.bartlett_window(10)
output = (input_data * window_data)