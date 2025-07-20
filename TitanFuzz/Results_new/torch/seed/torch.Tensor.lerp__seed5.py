input_tensor = torch.rand(2, 3)
end = torch.rand(2, 3)
weight = torch.rand(2, 3)
torch.Tensor.lerp_(input_tensor, end, weight)