input_tensor = torch.rand(3, 3)
end = torch.rand(3, 3)
weight = torch.rand(3, 3)
output_tensor = torch.Tensor.lerp(input_tensor, end, weight)