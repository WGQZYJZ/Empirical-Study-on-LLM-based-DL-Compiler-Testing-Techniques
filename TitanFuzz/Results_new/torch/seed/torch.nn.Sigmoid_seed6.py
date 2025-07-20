x = Variable(torch.Tensor([(- 1.0), 0.0, 1.0]), requires_grad=True)
y = torch.nn.Sigmoid()(x)
y.backward(torch.Tensor([1.0, 1.0, 1.0]))