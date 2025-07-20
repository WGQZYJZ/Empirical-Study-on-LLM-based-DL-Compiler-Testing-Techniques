window_length = 100
beta = 12.0
kaiser_window = torch.kaiser_window(window_length, periodic=True, beta=beta)