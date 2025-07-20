input_data = torch.tensor([[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]]])
pooling_layer = torch.nn.AvgPool2d(2, stride=2)
output = pooling_layer(input_data)