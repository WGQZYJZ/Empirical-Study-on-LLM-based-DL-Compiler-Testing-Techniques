input_data = torch.randn(2, 3)
log_softmax_output = torch.special.log_softmax(input_data, dim=1)