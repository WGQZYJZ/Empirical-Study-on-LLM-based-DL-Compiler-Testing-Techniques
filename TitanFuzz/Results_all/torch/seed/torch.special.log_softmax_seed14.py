input_data = torch.randn(3, requires_grad=True)
log_softmax = torch.special.log_softmax(input_data, dim=0)