input_data = torch.tensor([[True, False], [False, False]], dtype=torch.bool)
other_data = torch.tensor([[False, True], [True, False]], dtype=torch.bool)
output_data = torch.bitwise_or(input_data, other_data)