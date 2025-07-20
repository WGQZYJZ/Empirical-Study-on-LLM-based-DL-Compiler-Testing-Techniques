input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
index = torch.tensor([[0, 1], [1, 2]], dtype=torch.long)
output = torch.gather(input_data, dim=1, index=index)