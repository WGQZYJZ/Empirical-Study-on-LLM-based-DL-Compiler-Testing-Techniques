input_data = Variable(torch.randn(1, 1, 5))
output_data = torch.nn.functional.lp_pool1d(input_data, 1, 3, 2)
output_data = torch.nn.functional.lp_pool1d(input_data, 2, 3, 2)