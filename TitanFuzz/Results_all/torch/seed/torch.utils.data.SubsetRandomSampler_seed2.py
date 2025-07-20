input_data = torch.randint(low=0, high=100, size=(10,))
sampler = torch.utils.data.SubsetRandomSampler(indices=input_data)