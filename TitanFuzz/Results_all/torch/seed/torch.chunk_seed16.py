input_data = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
output = torch.chunk(input_data, 3, dim=1)