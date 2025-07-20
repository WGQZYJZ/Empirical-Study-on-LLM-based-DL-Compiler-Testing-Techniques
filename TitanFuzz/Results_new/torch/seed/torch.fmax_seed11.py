input_data = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
other_data = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)
output_data = torch.fmax(input_data, other_data)