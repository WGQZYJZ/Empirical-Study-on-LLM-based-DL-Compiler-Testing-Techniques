input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
vec2 = torch.tensor([1, 2, 3], dtype=torch.float)
out = torch.Tensor.outer(input_tensor, vec2)