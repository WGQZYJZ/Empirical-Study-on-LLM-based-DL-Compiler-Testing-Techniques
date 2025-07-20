input = torch.randn(1, 3)
output = torch.nn.functional.log_softmax(input, dim=1)