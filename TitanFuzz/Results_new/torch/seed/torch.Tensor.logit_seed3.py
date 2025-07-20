input_data = Variable(torch.randn(1, 1, 3, 3))
output_data = torch.Tensor.logit(input_data)