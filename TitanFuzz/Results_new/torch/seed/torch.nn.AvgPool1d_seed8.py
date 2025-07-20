input = torch.randn(2, 3, 5)
output = torch.nn.AvgPool1d(kernel_size=3, stride=1, padding=0)(input)
input = torch.randn(2, 3, 5, 5)
output = torch.nn.AvgPool2d(kernel_size=3, stride=1, padding=0)(input)