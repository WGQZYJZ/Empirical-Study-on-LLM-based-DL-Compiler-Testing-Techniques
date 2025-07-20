input_tensor = torch.randint(low=0, high=10, size=(5, 5), dtype=torch.float32)
neg_tensor = torch.Tensor.neg(input_tensor)