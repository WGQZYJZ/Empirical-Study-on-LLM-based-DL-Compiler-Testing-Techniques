input = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0], dtype=torch.float)
scale = 0.1
zero_point = 1
quant_min = 0
quant_max = 2
output = torch.fake_quantize_per_tensor_affine(input, scale, zero_point, quant_min, quant_max)