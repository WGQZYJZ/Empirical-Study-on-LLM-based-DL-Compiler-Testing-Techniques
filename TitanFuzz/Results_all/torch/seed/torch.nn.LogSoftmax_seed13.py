input_data = torch.randn(2, 3)
log_softmax = torch.nn.LogSoftmax(dim=1)
output_data = log_softmax(input_data)