input_tensor = torch.randint(0, 10, (3, 5))
torch.Tensor.narrow_copy(input_tensor, 1, 1, 2)