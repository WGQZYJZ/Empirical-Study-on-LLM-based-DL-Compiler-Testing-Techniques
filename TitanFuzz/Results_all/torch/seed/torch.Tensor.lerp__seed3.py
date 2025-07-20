input_tensor = torch.randn(1, 3)
end = torch.randn(1, 3)
weight = torch.randn(1, 3)
output_tensor = torch.Tensor.lerp_(input_tensor, end, weight)