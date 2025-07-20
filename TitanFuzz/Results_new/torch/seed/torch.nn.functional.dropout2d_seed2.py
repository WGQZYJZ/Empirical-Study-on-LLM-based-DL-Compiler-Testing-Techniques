input = torch.ones(1, 1, 3, 3)
output = torch.nn.functional.dropout2d(input, p=0.5, training=True, inplace=False)