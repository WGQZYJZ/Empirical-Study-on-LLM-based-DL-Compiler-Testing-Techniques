input_data = torch.arange(0, 10)
indices = [3, 4, 5]
output_data = torch.utils.data.Subset(input_data, indices)