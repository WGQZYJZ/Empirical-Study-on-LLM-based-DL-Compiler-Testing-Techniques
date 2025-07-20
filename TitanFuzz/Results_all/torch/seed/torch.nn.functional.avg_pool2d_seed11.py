input = torch.rand(1, 1, 3, 3)
output = torch.nn.functional.avg_pool2d(input, kernel_size=3, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)