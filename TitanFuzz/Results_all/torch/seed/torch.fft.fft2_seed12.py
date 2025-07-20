input_data = torch.randn(2, 3, 4, 5)
output_data = torch.fft.fft2(input_data, s=None, dim=((- 2), (- 1)), norm=None, out=None)