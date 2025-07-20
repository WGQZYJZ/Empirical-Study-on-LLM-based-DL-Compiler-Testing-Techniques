input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
end = torch.tensor([[2, 3, 4], [5, 6, 7], [8, 9, 10]], dtype=torch.float32)
weight = torch.tensor([0.5], dtype=torch.float32)
output_tensor = torch.Tensor.lerp_(input_tensor, end, weight)