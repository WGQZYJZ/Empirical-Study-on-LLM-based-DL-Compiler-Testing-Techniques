input_data = Variable(torch.randn(1, 1, 10, 10, 10))
output = torch.nn.functional.adaptive_max_pool3d(input_data, (3, 3, 3))