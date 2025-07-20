x = Variable(torch.randn(4, 4), requires_grad=True)
y = Variable(torch.randn(4, 4), requires_grad=True)
z = Variable(torch.randn(4, 4), requires_grad=True)
parameters = [x, y, z]
vector = torch.nn.utils.parameters_to_vector(parameters)