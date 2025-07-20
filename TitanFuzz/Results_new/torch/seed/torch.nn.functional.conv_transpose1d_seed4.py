input_data = torch.randn(1, 1, 3, requires_grad=True)
weight = torch.randn(1, 1, 2, requires_grad=True)
conv_transpose_output = torch.nn.functional.conv_transpose1d(input_data, weight, stride=2)