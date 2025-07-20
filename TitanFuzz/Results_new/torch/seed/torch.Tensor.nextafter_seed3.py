input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.nextafter(input_tensor, (input_tensor + 1))