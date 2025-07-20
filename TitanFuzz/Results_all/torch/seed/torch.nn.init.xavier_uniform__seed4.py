input_size = 5
output_size = 5
input_data = torch.randn(input_size, output_size)
torch.nn.init.xavier_uniform_(input_data)