input = torch.rand(1, 3, 4, 4)
output = torch.nn.functional.unfold(input, kernel_size=3, dilation=1, padding=0, stride=1)