input_tensor = torch.randn(2, 3)
output_tensor = torch.log1p(input_tensor)
output_tensor = torch.Tensor.log1p_(input_tensor)