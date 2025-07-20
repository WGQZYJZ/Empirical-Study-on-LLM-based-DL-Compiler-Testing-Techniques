input_data = Variable(torch.randn(1, 3, 224, 224))
input_data = Variable(torch.randn(1, 3, 224, 224))
output = torch.nn.Hardswish()(input_data)