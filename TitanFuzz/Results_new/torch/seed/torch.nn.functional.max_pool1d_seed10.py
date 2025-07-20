input_data = Variable(torch.randn(1, 1, 4))
output_data = torch.nn.functional.max_pool1d(input_data, kernel_size=2, stride=1)