w1 = Variable(torch.randn(2, 3), requires_grad=True)
w2 = Variable(torch.randn(3, 3), requires_grad=True)
vector = torch.nn.utils.parameters_to_vector([w1, w2])
w1 = Variable(torch.randn(2, 3), requires_grad=True)
w2 = Variable(torch.randn(3, 3), requires_grad=True)
vector = torch