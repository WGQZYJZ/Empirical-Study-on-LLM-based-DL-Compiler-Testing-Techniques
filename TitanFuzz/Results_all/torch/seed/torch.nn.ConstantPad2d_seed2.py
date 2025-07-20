input = Variable(torch.Tensor([[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]]]))
pad = torch.nn.ConstantPad2d((1, 2, 3, 4), 3)
output = pad(input)