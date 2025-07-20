input_data = torch.tensor([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]], dtype=torch.float32)
output_data = torch.cummax(input_data, dim=1)