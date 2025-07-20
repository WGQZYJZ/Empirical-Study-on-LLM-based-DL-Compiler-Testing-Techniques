input_tensor = torch.rand(4, 4)
end_tensor = torch.rand(4, 4)
weight = 0.5
output_tensor = torch.Tensor.lerp_(input_tensor, end_tensor, weight)