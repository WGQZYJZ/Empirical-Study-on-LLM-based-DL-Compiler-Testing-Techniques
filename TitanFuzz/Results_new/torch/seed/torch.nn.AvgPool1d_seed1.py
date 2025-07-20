input = Variable(torch.Tensor([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]]))
avgpool1d = torch.nn.AvgPool1d(kernel_size=2, stride=2)
output = avgpool1d(input)