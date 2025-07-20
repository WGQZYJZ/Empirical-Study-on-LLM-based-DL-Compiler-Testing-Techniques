window_length = 8
window = torch.kaiser_window(window_length, periodic=True, beta=12.0)