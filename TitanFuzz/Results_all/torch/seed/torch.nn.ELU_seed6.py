x = Variable(torch.Tensor([(- 1), 0, 1]))
y = torch.nn.ELU()(x)