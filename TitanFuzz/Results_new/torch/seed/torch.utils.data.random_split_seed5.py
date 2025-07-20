input_data = torch.randn(10, 2)
(train_data, test_data) = torch.utils.data.random_split(input_data, [7, 3])
(train_data, test_data) = torch.utils.data.random_split(input_data, [3, 7])
(train_data, test_data) = torch.utils.data.random_split(input_data, [3, 7])