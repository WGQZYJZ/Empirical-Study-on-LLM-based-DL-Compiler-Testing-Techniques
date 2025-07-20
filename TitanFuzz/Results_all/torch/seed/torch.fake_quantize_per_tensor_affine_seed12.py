input = Variable(torch.FloatTensor([[(- 63.0), (- 127.0), 63.0, 127.0]]))
output = torch.fake_quantize_per_tensor_affine(input, scale=1.0, zero_point=0, quant_min=0, quant_max=255)