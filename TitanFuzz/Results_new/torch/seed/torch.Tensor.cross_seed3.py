input_tensor = Variable(torch.randn(3, 4))
other = Variable(torch.randn(3, 4))
output_tensor = torch.Tensor.cross(input_tensor, other, dim=(- 1))