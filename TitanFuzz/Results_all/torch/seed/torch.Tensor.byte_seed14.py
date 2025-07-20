input_tensor = torch.rand(3, 3)
output_tensor = torch.Tensor.byte(input_tensor, memory_format=torch.preserve_format)