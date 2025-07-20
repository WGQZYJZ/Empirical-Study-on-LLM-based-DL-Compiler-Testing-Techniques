data = np.random.randint(0, 100, size=(100,))
random_sampler = torch.utils.data.RandomSampler(data)
for i in random_sampler:
    print('Index: ', i)