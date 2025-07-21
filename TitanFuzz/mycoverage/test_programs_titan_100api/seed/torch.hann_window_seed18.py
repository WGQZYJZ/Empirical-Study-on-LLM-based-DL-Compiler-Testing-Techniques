input_data = torch.rand(12)
hann_window = torch.hann_window(12)
output = (input_data * hann_window)