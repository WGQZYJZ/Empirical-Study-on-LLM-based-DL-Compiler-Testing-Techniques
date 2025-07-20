input = torch.randn(3, 3)
output = torch.fake_quantize_per_tensor_affine(input, scale=1.0, zero_point=0, quant_min=0, quant_max=255)