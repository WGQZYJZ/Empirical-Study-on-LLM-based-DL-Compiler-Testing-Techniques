input_data = Variable(torch.randn(5, 3))
output = torch.nn.LogSoftmax(dim=1)(input_data)