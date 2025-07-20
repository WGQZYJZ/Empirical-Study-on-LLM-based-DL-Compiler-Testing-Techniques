input = Variable(torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])).view(1, 1, 4, 4)
output = torch.nn.MaxPool2d(2, stride=2, padding=0)(input)