input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
index = torch.tensor([0, 2], dtype=torch.int64)
tensor = torch.tensor([[10, 20], [30, 40]], dtype=torch.float32)
torch.Tensor.index_add_(input_tensor, 0, index, tensor)