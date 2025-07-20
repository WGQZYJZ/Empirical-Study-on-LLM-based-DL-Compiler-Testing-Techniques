input_tensor = torch.randn(4, 4)
other = torch.randn(4, 4)
output_tensor = torch.Tensor.eq_(input_tensor, other)
output_tensor = torch.eq(input_tensor, other)