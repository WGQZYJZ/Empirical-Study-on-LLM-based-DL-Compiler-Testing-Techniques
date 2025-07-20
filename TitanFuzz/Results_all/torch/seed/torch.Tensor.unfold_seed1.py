input_tensor = torch.arange(0, 24).reshape(2, 3, 4)
result = torch.Tensor.unfold(input_tensor, 2, 3, 2)