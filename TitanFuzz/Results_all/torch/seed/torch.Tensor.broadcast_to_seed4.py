input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = torch.Tensor.broadcast_to(input_tensor, (3, 2, 3))