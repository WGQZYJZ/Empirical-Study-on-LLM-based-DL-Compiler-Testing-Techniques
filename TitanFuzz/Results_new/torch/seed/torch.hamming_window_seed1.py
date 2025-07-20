input_data = torch.rand(1, 10)
output = torch.hamming_window(10, periodic=True, alpha=0.54, beta=0.46)