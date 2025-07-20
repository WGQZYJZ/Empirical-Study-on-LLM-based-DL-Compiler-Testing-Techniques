input = torch.randn(2, 3, requires_grad=True)
output = torch.special.log_softmax(input, dim=1)
output.backward(torch.ones(2, 3))