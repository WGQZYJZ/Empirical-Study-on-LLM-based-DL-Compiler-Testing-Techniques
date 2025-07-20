input_data = torch.rand(10, 10)
output_data = torch.chain_matmul(input_data, input_data, input_data)