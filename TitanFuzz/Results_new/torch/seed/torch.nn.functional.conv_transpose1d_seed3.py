input = torch.randn(1, 1, 3, requires_grad=True)
weight = torch.randn(1, 1, 2, requires_grad=True)
output = torch.nn.functional.conv_transpose1d(input, weight, stride=1)
output.backward(torch.randn(1, 1, 4))