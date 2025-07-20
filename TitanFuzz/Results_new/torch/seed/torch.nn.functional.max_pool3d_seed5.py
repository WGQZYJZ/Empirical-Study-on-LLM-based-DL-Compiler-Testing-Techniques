input = Variable(torch.randn(1, 3, 5, 5, 5))
output = torch.nn.functional.max_pool3d(input, kernel_size=2, stride=2)