input = Variable(torch.Tensor([[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]]))
indices = Variable(torch.LongTensor([[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]]))
max_unpool = torch.nn.MaxUnpool1d(kernel_size=2, stride=2, padding=0)
output = max_unpool(input, indices)