input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
threshold = torch.nn.Threshold(3, 0)
output = threshold(input_data)