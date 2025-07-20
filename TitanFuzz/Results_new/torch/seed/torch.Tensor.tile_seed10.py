input_tensor = torch.randn(3, 5)
output_tensor = torch.Tensor.tile(input_tensor, dims=(2, 3))
output_tensor = torch.Tensor.tile(input_tensor, dims=(1, 3))