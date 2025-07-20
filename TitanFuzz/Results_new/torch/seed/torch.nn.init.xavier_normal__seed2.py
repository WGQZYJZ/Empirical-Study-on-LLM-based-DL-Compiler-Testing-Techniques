input_data = torch.randn(2, 3, dtype=torch.float)
torch.nn.init.xavier_normal_(input_data)