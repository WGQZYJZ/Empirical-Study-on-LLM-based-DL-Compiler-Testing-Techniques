input = Variable(torch.randn(1, 1, 2, 2))
indices = Variable(torch.LongTensor([[[[0, 1], [1, 0]]]]))
output = torch.nn.functional.max_unpool2d(input, indices, kernel_size=2, stride=1, padding=0)