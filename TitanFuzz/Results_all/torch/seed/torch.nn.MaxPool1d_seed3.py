input = Variable(torch.Tensor([[[1, 2, 3, 4, 5, 6, 7]]]))
maxpool = torch.nn.MaxPool1d(kernel_size=3, stride=1, padding=0)
output = maxpool(input)