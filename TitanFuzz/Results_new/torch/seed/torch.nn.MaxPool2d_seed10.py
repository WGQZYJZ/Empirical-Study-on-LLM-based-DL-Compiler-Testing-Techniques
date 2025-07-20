input = Variable(torch.Tensor([[[[1, 1, 1], [2, 2, 2], [3, 3, 3]]]]))
max_pooling = torch.nn.MaxPool2d(kernel_size=2, stride=1, padding=0)
output = max_pooling(input)