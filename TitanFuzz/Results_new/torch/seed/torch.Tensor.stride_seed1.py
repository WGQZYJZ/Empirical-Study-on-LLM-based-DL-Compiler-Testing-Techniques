input_tensor = torch.rand(2, 3, 4)
output_tensor = torch.Tensor.stride(input_tensor, dim=1)