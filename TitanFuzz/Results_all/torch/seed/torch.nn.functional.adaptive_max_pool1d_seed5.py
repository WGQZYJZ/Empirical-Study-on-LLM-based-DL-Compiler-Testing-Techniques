input_data = Variable(torch.randn(1, 1, 5))
output = torch.nn.functional.adaptive_max_pool1d(input_data, 2)
(output, indices) = torch.nn.functional.adaptive_max_pool1d(input_data, 2, return_indices=True)