input_data = [torch.arange(1, 7).reshape(2, 3), torch.arange(7, 13).reshape(2, 3)]
output_data = torch.block_diag(*input_data)