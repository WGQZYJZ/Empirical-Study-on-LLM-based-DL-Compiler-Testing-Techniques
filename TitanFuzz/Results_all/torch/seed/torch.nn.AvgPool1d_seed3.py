input_data = Variable(torch.Tensor([[1, 2, 3, 4, 5, 6, 7]]))
avg_pooling = torch.nn.AvgPool1d(kernel_size=3, stride=1, padding=0)
output = avg_pooling(input_data)