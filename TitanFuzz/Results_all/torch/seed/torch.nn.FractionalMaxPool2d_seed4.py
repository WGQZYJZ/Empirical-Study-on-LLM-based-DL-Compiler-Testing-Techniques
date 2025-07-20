input = Variable(torch.Tensor([[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]]))
output = torch.nn.FractionalMaxPool2d(3, output_ratio=[0.5, 0.5])(input)