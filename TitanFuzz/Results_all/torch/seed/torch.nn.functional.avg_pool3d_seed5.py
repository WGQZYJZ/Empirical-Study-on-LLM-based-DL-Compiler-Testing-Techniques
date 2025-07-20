input_data = torch.rand(1, 1, 3, 3, 3)
avg_pool3d_data = torch.nn.functional.avg_pool3d(input_data, kernel_size=2, stride=1, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)