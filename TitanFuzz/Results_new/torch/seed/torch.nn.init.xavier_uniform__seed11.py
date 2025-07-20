input_size = 10
output_size = 20
input_data = torch.randn(input_size, output_size)
torch.nn.init.xavier_uniform_(input_data, gain=1.0)