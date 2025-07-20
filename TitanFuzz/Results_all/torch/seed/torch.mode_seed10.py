input_data = torch.tensor([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 1, 1, 1, 1]])
output_data = torch.mode(input_data, dim=0, keepdim=False)