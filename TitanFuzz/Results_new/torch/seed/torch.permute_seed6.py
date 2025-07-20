input_data = torch.randn(2, 3, 4)
output_data = torch.permute(input_data, (1, 0, 2))
input_data = torch.randn(2, 3, 4)
output_data = torch.squeeze(input_data)