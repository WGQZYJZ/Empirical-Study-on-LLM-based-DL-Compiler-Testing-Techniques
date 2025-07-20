input_data = torch.rand(1, 1, 6)
m = torch.nn.AdaptiveMaxPool1d(3)
output = m(input_data)