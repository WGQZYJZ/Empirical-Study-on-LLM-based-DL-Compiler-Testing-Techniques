input_data = Variable(torch.rand(5, 10))
torch.nn.Hardshrink(lambd=0.5)(input_data)
input_data = Variable(torch.rand(5, 10))