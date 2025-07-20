input_tensor = torch.tensor([[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]], dtype=torch.uint8)
output_tensor = torch.Tensor.bitwise_not_(input_tensor)