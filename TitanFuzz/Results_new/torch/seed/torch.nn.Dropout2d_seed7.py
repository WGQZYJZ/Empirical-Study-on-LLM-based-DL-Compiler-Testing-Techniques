input_data = torch.ones(2, 2, requires_grad=True)
dropout_layer = torch.nn.Dropout2d(p=0.5, inplace=False)