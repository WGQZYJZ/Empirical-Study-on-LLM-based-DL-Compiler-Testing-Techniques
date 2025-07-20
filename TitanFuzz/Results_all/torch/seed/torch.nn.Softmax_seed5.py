input_data = Variable(torch.randn(5, 3))
softmax_output = torch.nn.Softmax(dim=1)(input_data)