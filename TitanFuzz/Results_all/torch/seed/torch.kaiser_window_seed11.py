window_length = 5
periodic = True
beta = 12.0
window = torch.kaiser_window(window_length, periodic=periodic, beta=beta)
window_np = np.kaiser(window_length, beta)