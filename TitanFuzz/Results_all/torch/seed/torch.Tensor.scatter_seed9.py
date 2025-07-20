input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
index = torch.tensor([[0, 1], [1, 2]], dtype=torch.long)
src = torch.tensor([2, 3], dtype=torch.float32)
output_tensor = torch.Tensor.scatter(input_tensor, 0, index, src)