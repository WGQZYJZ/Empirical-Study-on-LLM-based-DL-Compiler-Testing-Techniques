input_data = torch.randn(1, 3, 32, 32)
output_data = torch.nn.init.kaiming_normal_(input_data)
input_data = torch.randn(1, 3, 32, 32)
output_data = torch.nn.init.kaiming_normal_(input_data, nonlinearity='relu')