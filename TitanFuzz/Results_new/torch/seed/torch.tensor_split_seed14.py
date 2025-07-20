input_tensor = torch.randn(3, 5, 7)
output_tensor = torch.tensor_split(input_tensor, 3, dim=2)