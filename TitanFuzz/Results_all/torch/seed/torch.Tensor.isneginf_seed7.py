input_tensor = torch.tensor([float('-inf'), float('inf'), float('nan')])
output_tensor = torch.Tensor.isneginf(input_tensor)