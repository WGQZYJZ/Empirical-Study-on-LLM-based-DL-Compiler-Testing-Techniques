input_tensor = torch.randn(4, 4)
end = torch.randn(4, 4)
weight = torch.randn(4, 4)
torch.Tensor.lerp_(input_tensor, end, weight)