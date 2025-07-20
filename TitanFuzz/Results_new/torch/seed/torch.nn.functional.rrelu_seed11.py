input = torch.randn(3, 5)
output = torch.nn.functional.rrelu(input, lower=(1.0 / 8), upper=(1.0 / 3), training=False, inplace=False)
output = torch.nn.functional.rrelu(input, lower=(1.0 / 8), upper=(1.0 / 3), training=True, inplace=False)
output = torch.nn.functional.rrelu(input, lower=(1.0 / 8), upper=(1.0 / 3), training=True, inplace=True)