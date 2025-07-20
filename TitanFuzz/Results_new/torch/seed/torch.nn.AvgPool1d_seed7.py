input_data = torch.randn(1, 1, 4)
avg_pool1d = torch.nn.AvgPool1d(kernel_size=2, stride=1, padding=1, ceil_mode=True, count_include_pad=False)
output = avg_pool1d(input_data)