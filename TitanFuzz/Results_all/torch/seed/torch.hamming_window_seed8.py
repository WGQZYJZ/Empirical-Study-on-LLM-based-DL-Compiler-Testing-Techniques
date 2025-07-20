window_length = 10
periodic = True
alpha = 0.54
beta = 0.46
hamming_window = torch.hamming_window(window_length, periodic, alpha, beta)