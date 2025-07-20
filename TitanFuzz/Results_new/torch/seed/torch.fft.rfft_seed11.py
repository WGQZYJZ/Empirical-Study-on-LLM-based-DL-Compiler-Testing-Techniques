input_data = torch.tensor([1.0, 2.0, 3.0, 4.0])
output = torch.fft.rfft(input_data)
output = torch.fft.irfft(input_data)