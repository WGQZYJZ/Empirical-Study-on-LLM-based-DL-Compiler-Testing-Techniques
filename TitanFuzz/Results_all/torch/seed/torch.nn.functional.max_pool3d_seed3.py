input_data = Variable(torch.randn(1, 1, 10, 10, 10))
output = torch.nn.functional.max_pool3d(input_data, kernel_size=2, stride=2)