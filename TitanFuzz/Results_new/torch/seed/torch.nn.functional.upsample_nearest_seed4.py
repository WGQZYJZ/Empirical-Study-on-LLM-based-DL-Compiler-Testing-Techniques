input_data = torch.rand(1, 1, 4, 4)
input = Variable(input_data, requires_grad=True)
output = torch.nn.functional.upsample_nearest(input, size=None, scale_factor=2)
output.backward(torch.ones(output.size()))