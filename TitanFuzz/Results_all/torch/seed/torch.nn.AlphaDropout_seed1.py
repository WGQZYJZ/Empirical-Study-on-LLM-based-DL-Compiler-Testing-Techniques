input_data = torch.randn(1, 1, 3, 3)
alpha_dropout = torch.nn.AlphaDropout(p=0.5, inplace=False)
output = alpha_dropout(input_data)