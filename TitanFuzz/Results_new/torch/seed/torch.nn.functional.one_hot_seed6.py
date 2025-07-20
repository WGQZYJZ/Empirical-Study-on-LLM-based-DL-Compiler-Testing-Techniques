input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
output = torch.nn.functional.one_hot(input_data, num_classes=10)