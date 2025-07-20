input_tensor = torch.rand(4, 4)
end = torch.rand(4, 4)
weight = 0.5
torch.Tensor.lerp_(input_tensor, end, weight)