input_data = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
output_data = torch.normal(mean=input_data, std=torch.ones(input_data.size()))