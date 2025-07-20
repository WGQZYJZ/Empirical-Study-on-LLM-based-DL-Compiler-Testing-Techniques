input_data = torch.randn(1, 1, 3)
output_data = torch.nn.LazyConvTranspose1d(1, 1, stride=1, padding=0, output_padding=0, groups=1, bias=True, dilation=1, padding_mode='zeros', device=None, dtype=None)(input_data)
output_data = torch.nn.LazyConvTranspose1d(1, 1, stride=1, padding=0, output_padding=0, groups=1, bias=True, dilation=1, padding_mode='zeros', device=None, dtype=None)(input_data)