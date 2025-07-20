input_tensor = torch.randn(2, 3, 4, 5)
input_tensor = torch.randn(2, 3, 4, 5)
output_tensor = torch.Tensor.as_subclass(input_tensor, torch.Tensor)