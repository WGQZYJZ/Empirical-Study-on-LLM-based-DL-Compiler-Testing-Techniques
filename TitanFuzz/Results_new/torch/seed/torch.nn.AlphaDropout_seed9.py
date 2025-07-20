input_data = torch.randn(3, 3, requires_grad=True)
dropout = torch.nn.AlphaDropout(p=0.5, inplace=False)
output = dropout(input_data)