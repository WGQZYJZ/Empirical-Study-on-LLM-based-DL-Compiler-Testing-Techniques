input_tensor = torch.Tensor([180, 90, 0, (- 90), (- 180)])
output_tensor = torch.Tensor.deg2rad(input_tensor)