input = Variable(torch.Tensor([[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]]]))
max_pool2d = torch.nn.MaxPool2d(kernel_size=2, stride=2)
output = max_pool2d(input)