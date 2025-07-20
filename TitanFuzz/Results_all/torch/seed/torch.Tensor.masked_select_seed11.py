if True:
    input_tensor = torch.randn(3, 4)
    mask = torch.ByteTensor([[0, 0, 1, 0], [1, 1, 1, 1], [1, 0, 0, 1]])
    mask_tensor = torch.Tensor.masked_select(input_tensor, mask)
    print(input_tensor)
    print(mask_tensor)