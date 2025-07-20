input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vec2 = torch.tensor([1, 2, 3])
output_tensor = torch.Tensor.outer(input_tensor, vec2)