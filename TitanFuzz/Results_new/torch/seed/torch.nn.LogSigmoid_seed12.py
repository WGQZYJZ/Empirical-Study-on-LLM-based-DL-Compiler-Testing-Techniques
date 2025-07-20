input_data = torch.tensor([[0.2, 0.4, 0.6]])
log_sigmoid = torch.nn.LogSigmoid()
output = log_sigmoid(input_data)