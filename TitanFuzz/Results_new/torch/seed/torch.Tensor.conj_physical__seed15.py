if True:
    import torch
    input_tensor = torch.randint(low=0, high=10, size=(3, 4), dtype=torch.int32)
    print('Input: ', input_tensor)
    torch.Tensor.conj_physical_(input_tensor)
    print('Output: ', input_tensor)