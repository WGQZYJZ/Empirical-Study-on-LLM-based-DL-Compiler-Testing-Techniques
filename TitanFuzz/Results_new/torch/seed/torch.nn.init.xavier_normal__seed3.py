input_size = 10
batch_size = 3
input_data = torch.randn(batch_size, input_size)
torch.nn.init.xavier_normal_(input_data)