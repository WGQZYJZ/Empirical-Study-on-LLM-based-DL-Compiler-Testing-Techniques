input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.uint8)
output_tensor = torch.Tensor.bitwise_left_shift_(input_tensor, 2)