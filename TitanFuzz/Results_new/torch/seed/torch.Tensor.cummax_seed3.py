input_tensor = torch.randint(low=0, high=10, size=(2, 3, 4), dtype=torch.int32)
cummax_tensor = torch.Tensor.cummax(input_tensor, dim=2)