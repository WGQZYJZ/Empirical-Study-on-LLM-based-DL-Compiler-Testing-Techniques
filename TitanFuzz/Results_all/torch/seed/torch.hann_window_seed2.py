window_length = 10
input_data = torch.rand(window_length)
output = torch.hann_window(window_length)