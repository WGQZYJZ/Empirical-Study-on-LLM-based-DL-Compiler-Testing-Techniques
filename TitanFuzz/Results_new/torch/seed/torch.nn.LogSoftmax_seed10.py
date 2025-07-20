input = torch.randn(2, 3, requires_grad=True)
output = torch.nn.LogSoftmax(dim=1)(input)
output_expected = torch.log_softmax(input, dim=1)