input = Variable(torch.randn(1, 1, 3))
output = torch.nn.functional.conv_transpose1d(input, torch.randn(1, 1, 2))