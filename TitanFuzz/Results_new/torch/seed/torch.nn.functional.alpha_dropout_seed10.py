input = torch.randn(1, 3, 5)
output = torch.nn.functional.alpha_dropout(input, p=0.5, training=False, inplace=False)