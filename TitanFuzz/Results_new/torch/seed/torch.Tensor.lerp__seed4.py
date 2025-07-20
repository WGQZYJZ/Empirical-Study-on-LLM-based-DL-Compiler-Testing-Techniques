input_tensor = torch.rand(1, 3)
end = torch.rand(1, 3)
weight = torch.rand(1, 1)
output_tensor = torch.Tensor.lerp_(input_tensor, end, weight)