if True:
    input_tensor = torch.randn(4, 3)
    other = torch.randn(3)
    print(torch.Tensor.inner(input_tensor, other))