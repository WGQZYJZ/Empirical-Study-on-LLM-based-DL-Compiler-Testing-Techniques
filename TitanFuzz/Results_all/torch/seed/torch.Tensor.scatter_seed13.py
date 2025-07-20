input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
index = torch.tensor([0, 2], dtype=torch.long)
src = torch.tensor([[10, 11, 12], [13, 14, 15]], dtype=torch.float)
output_tensor = torch.Tensor.scatter(input_tensor, dim=0, index=index, src=src)