input_data = torch.randn(3, 4)
output = torch.linalg.matrix_norm(input_data, ord='fro')