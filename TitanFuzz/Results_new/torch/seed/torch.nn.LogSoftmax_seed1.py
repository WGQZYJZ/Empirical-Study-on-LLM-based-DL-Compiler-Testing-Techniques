input_data = torch.randn(2, 3)
output_data = torch.nn.LogSoftmax(dim=1)(input_data)