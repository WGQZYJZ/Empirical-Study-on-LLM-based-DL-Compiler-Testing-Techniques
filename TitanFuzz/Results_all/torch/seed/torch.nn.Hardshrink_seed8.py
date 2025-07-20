input_data = Variable(torch.Tensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]))
input_data = Variable(torch.Tensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]))
hardshrink = torch.nn.Hardshrink(lambd=0.5)
output = hardshrink(input_data)