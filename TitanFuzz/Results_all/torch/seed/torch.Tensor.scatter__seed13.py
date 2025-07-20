input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
dim = 0
index = torch.tensor([0, 2])
src = torch.tensor([[10, 11, 12], [13, 14, 15]])
output_tensor = torch.Tensor.scatter_(input_tensor, dim, index, src)