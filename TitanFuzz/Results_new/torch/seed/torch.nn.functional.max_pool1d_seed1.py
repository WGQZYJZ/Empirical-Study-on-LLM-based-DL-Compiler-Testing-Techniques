input_data = Variable(torch.randn(1, 1, 3))
output = torch.nn.functional.max_pool1d(input_data, 2)