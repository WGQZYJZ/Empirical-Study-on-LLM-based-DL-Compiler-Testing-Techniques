input_tensor = torch.randint(low=0, high=10, size=(2, 3), dtype=torch.int32)
torch.Tensor.remainder_(input_tensor, divisor=2)