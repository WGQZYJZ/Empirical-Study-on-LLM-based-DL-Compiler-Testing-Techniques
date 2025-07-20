input_data = torch.randn(1, 2, 3, 4)
output_data = torch.fft.irfftn(input_data, s=None, dim=None, norm=None, out=None)