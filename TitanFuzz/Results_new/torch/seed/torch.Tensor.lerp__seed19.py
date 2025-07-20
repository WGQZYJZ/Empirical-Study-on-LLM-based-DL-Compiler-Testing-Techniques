input_tensor = torch.rand(4, 4)
end_tensor = torch.rand(4, 4)
weight = 0.5
output = torch.Tensor.lerp_(input_tensor, end_tensor, weight)