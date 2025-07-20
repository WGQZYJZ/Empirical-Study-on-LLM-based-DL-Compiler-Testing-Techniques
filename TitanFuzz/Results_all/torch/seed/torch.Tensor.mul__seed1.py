input_tensor = torch.randint(1, 10, (3, 3), dtype=torch.int32)
torch.Tensor.mul_(input_tensor, 2)