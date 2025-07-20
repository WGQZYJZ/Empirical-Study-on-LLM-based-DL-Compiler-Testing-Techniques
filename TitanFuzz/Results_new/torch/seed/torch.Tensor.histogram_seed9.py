input_tensor = torch.randn(1, 10)
input = input_tensor.numpy()
bins = 10
range = ((- 10), 10)
weight = None
density = False
output = torch.Tensor.histogram(input_tensor, input, bins, range=range, weight=weight, density=density)