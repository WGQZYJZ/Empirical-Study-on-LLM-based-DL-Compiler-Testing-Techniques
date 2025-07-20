input_data = torch.randn(5, 3)
selu_layer = torch.nn.SELU(inplace=False)
output = selu_layer(input_data)