input_tensor = torch.randn(2, 6)
output_tensor = torch.Tensor.vsplit(input_tensor, 2)