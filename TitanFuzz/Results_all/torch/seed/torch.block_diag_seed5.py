input_data = [[1, 2, 3], [4, 5, 6]]
input_data = torch.tensor(input_data)
output = torch.block_diag(input_data)