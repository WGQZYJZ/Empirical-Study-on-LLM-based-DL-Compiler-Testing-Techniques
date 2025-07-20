input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
divisor = 2
output_tensor = torch.Tensor.fmod_(input_tensor, divisor)