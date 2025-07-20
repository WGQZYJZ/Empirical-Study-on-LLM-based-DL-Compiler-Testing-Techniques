input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
vec1 = torch.tensor([1, 2, 3], dtype=torch.float32)
vec2 = torch.tensor([4, 5, 6], dtype=torch.float32)
torch.Tensor.addr_(input_tensor, vec1, vec2, beta=1, alpha=1)
input