input = torch.randn(2, 3, requires_grad=True)
output = torch.special.log_softmax(input, dim=0)