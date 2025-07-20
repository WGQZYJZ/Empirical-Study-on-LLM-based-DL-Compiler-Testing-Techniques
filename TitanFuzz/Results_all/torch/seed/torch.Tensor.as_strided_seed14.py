input_tensor = torch.arange(0, 10)
out_tensor = torch.Tensor.as_strided(input_tensor, size=(2, 5), stride=(5, 1))