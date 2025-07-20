input = torch.randn(1, 1, 6, requires_grad=True)
output = torch.nn.functional.avg_pool1d(input, kernel_size=3, stride=2)