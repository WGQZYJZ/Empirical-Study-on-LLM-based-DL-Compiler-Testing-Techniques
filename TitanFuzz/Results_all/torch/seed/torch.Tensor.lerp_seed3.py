input_tensor = torch.randn(3, 3)
end = torch.randn(3, 3)
weight = torch.randn(1)
output_tensor = torch.Tensor.lerp(input_tensor, end, weight)