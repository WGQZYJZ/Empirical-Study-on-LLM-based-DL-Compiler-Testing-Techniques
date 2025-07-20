input = torch.randn(2, 3)
output = torch.nn.functional.log_softmax(input, dim=1)
output = torch.nn.functional.log_softmax(input, dim=0)
output = torch.nn.functional.log_softmax(input, dim=None)