input_data = torch.tensor([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
output_data = torch.moveaxis(input_data, 0, 1)