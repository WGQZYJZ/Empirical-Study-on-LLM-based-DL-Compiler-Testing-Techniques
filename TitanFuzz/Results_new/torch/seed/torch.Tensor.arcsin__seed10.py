input_tensor = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
arcsin_result = torch.Tensor.arcsin_(input_tensor)
for i in input_tensor:
    print('The result of math.asin is: ', math.asin(i))