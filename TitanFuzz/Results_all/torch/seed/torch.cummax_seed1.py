input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
cum_max_data = torch.cummax(input_data, dim=1)