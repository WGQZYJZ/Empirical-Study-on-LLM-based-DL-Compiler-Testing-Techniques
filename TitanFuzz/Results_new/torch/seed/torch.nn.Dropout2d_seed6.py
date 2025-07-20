input_data = torch.randn(1, 1, 4, 4)
dropout_layer = torch.nn.Dropout2d(p=0.5, inplace=False)
output = dropout_layer(input_data)