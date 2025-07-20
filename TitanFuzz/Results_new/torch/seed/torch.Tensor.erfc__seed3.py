input_tensor = Variable(torch.randn(3, 3))
output_tensor = torch.Tensor.erfc_(input_tensor)