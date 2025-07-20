input_data = Variable(torch.randn(1, 1, 5))
avg_pool1d = torch.nn.AvgPool1d(kernel_size=2, stride=2)
output = avg_pool1d(input_data)