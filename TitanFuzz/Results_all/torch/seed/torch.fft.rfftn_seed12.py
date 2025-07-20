input_data = torch.rand(2, 3, 4)
output_data = torch.fft.rfftn(input_data, s=(4,), dim=2, norm=None, out=None)