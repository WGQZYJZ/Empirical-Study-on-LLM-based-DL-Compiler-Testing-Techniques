input_tensor = torch.randn(4, 4)
end = torch.randn(4, 4)
weight = 0.5
output_tensor = torch.Tensor.lerp_(input_tensor, end, weight)