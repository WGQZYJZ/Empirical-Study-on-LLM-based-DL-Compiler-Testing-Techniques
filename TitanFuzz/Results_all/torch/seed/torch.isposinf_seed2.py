input_data = torch.Tensor([float('inf'), float('-inf'), float('nan'), (- 1), 0, 1])
result = torch.isposinf(input_data)