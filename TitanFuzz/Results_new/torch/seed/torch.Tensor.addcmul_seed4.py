if True:
    input_tensor = torch.randn(4, 4)
    tensor1 = torch.randn(4, 4)
    tensor2 = torch.randn(4, 4)
    output_tensor = torch.Tensor.addcmul(input_tensor, tensor1, tensor2)
    print(output_tensor)