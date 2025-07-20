input = torch.rand(3, 4)
torch.fake_quantize_per_tensor_affine(input, scale=0.5, zero_point=2, quant_min=0, quant_max=5)
input = torch.rand(3, 4)