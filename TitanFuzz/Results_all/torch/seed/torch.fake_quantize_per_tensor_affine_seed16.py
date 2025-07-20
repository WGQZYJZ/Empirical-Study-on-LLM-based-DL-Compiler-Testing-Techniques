input = torch.rand(4, dtype=torch.float)
scale = 1.0
zero_point = 0
quant_min = 0
quant_max = 255
output = torch.fake_quantize_per_tensor_affine(input, scale, zero_point, quant_min, quant_max)