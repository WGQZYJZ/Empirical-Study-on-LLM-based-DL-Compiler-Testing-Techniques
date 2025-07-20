input = torch.randn(20, 16, 32, 32)
output = torch.nn.functional.dropout2d(input, p=0.5, training=True, inplace=False)