input_tensor = torch.tensor([(- float('inf')), (- 2), (- 1), 0, 1, 2, float('inf')])
output_tensor = torch.Tensor.isneginf(input_tensor)