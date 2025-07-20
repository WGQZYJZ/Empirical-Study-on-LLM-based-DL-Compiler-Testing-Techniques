input = torch.randn(1, 1, 5, 5)
torch.nn.functional.unfold(input, kernel_size=3, dilation=1, padding=0, stride=1)