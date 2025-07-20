input_data = torch.rand(3, 4, 5)
output_data = torch.einsum('ijk, ilk -> ijl', input_data, input_data)