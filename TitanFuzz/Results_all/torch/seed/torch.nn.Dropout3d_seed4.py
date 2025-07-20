input_size = (1, 1, 2, 2, 2)
input_data = Variable(torch.randn(input_size))
dropout = torch.nn.Dropout3d(p=0.5, inplace=False)
output = dropout(input_data)