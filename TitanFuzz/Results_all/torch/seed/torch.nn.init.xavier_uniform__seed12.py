input_size = (1, 4, 4)
input_data = torch.randn(input_size)
torch.nn.init.xavier_uniform_(input_data)