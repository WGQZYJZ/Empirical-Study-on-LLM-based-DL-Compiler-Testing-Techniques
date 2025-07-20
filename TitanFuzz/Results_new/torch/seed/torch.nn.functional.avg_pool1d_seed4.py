x = torch.randn(2, 2, 4)
y = torch.nn.functional.avg_pool1d(x, kernel_size=2, stride=1, padding=0)