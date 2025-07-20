input = Variable(torch.randn(1, 4, 4))
indices = Variable(torch.LongTensor([[[1, 2, 1, 2], [2, 1, 2, 1], [1, 2, 1, 2], [2, 1, 2, 1]]]))
kernel_size = 2
output = torch.nn.functional.max_unpool1d(input, indices, kernel_size)