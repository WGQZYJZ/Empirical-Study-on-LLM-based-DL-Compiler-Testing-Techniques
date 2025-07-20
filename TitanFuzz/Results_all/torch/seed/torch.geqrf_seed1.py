input_data = torch.Tensor(np.random.rand(3, 3))
(q, r) = torch.geqrf(input_data)