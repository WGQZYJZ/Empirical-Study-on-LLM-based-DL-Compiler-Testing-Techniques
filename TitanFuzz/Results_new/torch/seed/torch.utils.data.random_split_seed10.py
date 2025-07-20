input_data = torch.randn(100, 10)
split_data = torch.utils.data.random_split(input_data, [20, 80])