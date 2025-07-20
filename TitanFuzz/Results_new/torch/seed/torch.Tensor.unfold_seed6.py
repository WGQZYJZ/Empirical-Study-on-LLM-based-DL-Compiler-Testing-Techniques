input_tensor = Variable(torch.randn(2, 3, 5, 7))
output_tensor = torch.Tensor.unfold(input_tensor, 2, 2, 1)