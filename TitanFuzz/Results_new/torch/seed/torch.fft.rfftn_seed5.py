input_data = torch.rand(10, 10, 10)
torch.fft.rfftn(input_data)
torch.fft.irfftn(input_data)