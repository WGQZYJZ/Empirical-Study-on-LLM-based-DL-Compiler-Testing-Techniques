input_tensor = Variable(torch.randn(5, 5))
other = Variable(torch.randn(5, 5))
output_tensor = torch.Tensor.atanh_(input_tensor, other)