input_data = torch.zeros(5, 3, dtype=torch.long)
output_data = torch.empty(5, 3)
torch.add(input_data, input_data, out=output_data)
input_data.add_(input_data)