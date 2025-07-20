input = torch.randn(20, 16, 50, dtype=torch.float)
weight = torch.randn(16, 3, 5, dtype=torch.float)
output = torch.nn.functional.conv_transpose1d(input, weight, bias=None, stride=1, padding=0, output_padding=0, groups=1, dilation=1)