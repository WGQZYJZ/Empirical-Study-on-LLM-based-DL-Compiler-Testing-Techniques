input = np.random.rand(2, 3, 4)
input = torch.Tensor(input)
output = torch.nn.functional.tanhshrink(input)