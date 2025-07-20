if True:
    mat1 = torch.rand(5, 3)
    mat2 = torch.rand(3, 4)
    _input_tensor = torch.rand(5, 4)
    _output_tensor = torch.Tensor.addmm(_input_tensor, mat1, mat2, beta=1, alpha=1)
    print(_output_tensor)