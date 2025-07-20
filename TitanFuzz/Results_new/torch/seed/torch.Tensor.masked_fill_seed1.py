input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
mask = torch.tensor([[0, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=torch.bool)
value = torch.tensor(100)
output_tensor = torch.Tensor.masked_fill(input_tensor, mask, value)