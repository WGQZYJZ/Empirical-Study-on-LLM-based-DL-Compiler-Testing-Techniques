input_data = torch.randn(1, 1, 5)
avgpool = torch.nn.AvgPool1d(kernel_size=3, stride=1, padding=0, ceil_mode=False, count_include_pad=True)