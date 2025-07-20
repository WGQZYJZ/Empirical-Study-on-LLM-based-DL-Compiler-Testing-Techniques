input_data = torch.arange(1, 101).view(10, 10)
(train_dataset, test_dataset) = torch.utils.data.random_split(input_data, [8, 2])