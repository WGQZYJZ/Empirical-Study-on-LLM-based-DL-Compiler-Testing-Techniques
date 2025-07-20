input = torch.randn(20, 16, 50)
output = torch.nn.functional.avg_pool1d(input, kernel_size=2)
output = torch.nn.functional.avg_pool1d(input, kernel_size=2, stride=2)
output = torch.nn.functional.avg_pool1d(input, kernel_size=2, stride=2, padding=1)