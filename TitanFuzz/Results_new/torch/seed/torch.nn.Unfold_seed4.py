input_data = torch.randn(1, 1, 5, 5)
unfold = torch.nn.Unfold(kernel_size=3, dilation=1, padding=0, stride=1)