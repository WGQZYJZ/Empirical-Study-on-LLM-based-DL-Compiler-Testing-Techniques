input_tensor = torch.rand(4, 4)
vec1 = torch.rand(4)
vec2 = torch.rand(4)
torch.Tensor.addr_(input_tensor, vec1, vec2)