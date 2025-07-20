input_tensor = torch.rand(4, 4)
end = torch.rand(4, 4)
weight = 0.5
output_tensor = torch.Tensor.lerp(input_tensor, end, weight)