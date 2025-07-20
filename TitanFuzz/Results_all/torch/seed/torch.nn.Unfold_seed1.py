input = torch.randn(1, 1, 4, 4)
unfold = torch.nn.Unfold(kernel_size=2, dilation=1, padding=0, stride=1)
output = unfold(input)