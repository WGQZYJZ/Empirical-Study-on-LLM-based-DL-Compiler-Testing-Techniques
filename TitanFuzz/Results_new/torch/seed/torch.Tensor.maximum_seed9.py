input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
other = torch.tensor([[10, 20, 30], [40, 50, 60]], dtype=torch.float32)
torch.Tensor.maximum(input_tensor, other)