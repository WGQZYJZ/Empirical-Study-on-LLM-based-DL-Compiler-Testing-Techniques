input_data = torch.randint(low=0, high=2, size=(5, 5), dtype=torch.int8)
logit_output = torch.Tensor.logit(input_data)