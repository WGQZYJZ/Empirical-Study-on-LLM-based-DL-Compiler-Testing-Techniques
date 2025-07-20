input_data = torch.tensor([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]], dtype=torch.float)
max_pool_1d = torch.nn.MaxPool1d(3, stride=2)
output = max_pool_1d(input_data.unsqueeze(0))