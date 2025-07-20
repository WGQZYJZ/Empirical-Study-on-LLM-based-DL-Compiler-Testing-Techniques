input_tensor = torch.tensor([float('inf'), float('-inf'), float('nan'), float('inf'), float('inf')])
result = torch.Tensor.isposinf(input_tensor)