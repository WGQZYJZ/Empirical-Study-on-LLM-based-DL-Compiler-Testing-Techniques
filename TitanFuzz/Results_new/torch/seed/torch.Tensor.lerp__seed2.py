input_tensor = torch.tensor([[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]])
end = torch.tensor([[0.9, 0.8, 0.7], [0.6, 0.5, 0.4]])
weight = 0.5
torch.Tensor.lerp_(input_tensor, end, weight)
torch.lerp(input_tensor, end, weight)
input_tensor.lerp_(end, weight)