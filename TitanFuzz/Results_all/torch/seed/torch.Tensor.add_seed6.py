input_tensor = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
other = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)
torch.Tensor.add(input_tensor, other)
torch.Tensor.add(input_tensor, other, alpha=0.5)