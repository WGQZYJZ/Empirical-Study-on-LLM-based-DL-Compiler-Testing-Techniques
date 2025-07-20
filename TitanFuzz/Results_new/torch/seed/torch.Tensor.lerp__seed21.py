input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
end = torch.tensor([[10, 20, 30], [40, 50, 60]])
weight = 0.5
output_tensor = torch.Tensor.lerp_(input_tensor, end, weight)