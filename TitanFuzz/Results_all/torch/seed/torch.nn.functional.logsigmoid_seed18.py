input = torch.randn(2, 3)
output = torch.nn.functional.logsigmoid(input)
input = torch.randn(2, 3)
output = torch.nn.functional.log_softmax(input, dim=1)