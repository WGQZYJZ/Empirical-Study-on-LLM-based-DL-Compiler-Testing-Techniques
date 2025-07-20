input = torch.randn(2, 3, requires_grad=True)
output = torch.nn.functional.log_softmax(input, dim=1)