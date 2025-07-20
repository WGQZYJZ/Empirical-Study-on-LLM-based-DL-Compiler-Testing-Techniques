input_data = torch.randn(2, 3)
relu = torch.nn.RReLU(lower=0.125, upper=0.3333333333333333, inplace=False)
output = relu(input_data)