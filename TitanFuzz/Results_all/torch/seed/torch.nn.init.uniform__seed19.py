input_data = torch.randn(2, 3)
torch.nn.init.uniform_(input_data, a=0.0, b=1.0)
input_data = torch.randn(2, 3)
torch.nn.init.normal_(input_data, mean=0.0, std=1.0)
input_data = torch.rand