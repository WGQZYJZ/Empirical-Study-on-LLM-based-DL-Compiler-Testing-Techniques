window_length = 10
window = torch.kaiser_window(window_length, periodic=True, beta=12.0)