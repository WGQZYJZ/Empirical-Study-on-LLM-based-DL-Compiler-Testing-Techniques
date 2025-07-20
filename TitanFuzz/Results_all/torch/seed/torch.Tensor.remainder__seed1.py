input_tensor = torch.randint(low=0, high=10, size=(1,), dtype=torch.float)
remainder = torch.Tensor.remainder_(input_tensor, 2)