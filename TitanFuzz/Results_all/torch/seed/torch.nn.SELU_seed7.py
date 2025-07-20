input_data = torch.randn(10)
output_data = torch.nn.SELU(inplace=False)(input_data)