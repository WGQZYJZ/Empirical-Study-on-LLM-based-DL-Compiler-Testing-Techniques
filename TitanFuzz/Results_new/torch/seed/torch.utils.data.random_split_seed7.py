input_data = torch.rand(5, 3)
(train_data, test_data) = torch.utils.data.random_split(input_data, [3, 2])