input_data = torch.randn(3, 3)
output = torch.nn.functional.rrelu(input_data, lower=(1.0 / 8), upper=(1.0 / 3), training=False, inplace=False)