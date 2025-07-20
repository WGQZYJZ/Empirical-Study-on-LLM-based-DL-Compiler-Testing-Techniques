input_tensor = torch.randn(3, 3)
end = torch.randn(3, 3)
weight = torch.rand(1)
output_tensor = torch.Tensor.lerp_(input_tensor, end, weight)