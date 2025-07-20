input_data = torch.rand(3, 3)
output_data = torch.hamming_window(input_data.size()[0], periodic=True, alpha=0.54, beta=0.46)