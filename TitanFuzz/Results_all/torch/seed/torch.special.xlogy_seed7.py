input_data = torch.tensor([[0.1, 0.2], [0.3, 0.4]])
other_data = torch.tensor([[0.5, 0.6], [0.7, 0.8]])
output_data = torch.special.xlogy(input_data, other_data)