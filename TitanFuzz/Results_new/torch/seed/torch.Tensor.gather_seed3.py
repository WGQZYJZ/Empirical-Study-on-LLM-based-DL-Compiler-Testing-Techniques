input_tensor = torch.randn(4, 5)
index = torch.tensor([1, 3], dtype=torch.long)
output_tensor = torch.Tensor.gather(input_tensor, 0, index)