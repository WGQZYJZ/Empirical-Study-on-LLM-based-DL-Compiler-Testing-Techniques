input_data = torch.tensor([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
output_data = torch.nn.functional.one_hot(input_data)