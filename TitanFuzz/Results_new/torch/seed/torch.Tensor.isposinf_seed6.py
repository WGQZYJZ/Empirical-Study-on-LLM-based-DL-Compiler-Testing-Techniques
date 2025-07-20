input_tensor = torch.tensor([(- 1), 0, 1, float('inf'), float('nan')])
isposinf_output = torch.Tensor.isposinf(input_tensor)