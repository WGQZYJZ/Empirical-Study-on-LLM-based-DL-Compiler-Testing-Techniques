input = Variable(torch.LongTensor([[1, 2, 4, 5], [4, 3, 2, 9]]))
weight = Variable(torch.randn(10, 3))
output = torch.nn.functional.embedding_bag(input, weight, mode='mean')