x = np.arange(0, 24).reshape((2, 3, 4))
batch_size = 2
sampler = torch.utils.data.BatchSampler(torch.utils.data.SequentialSampler(range(x.shape[0])), batch_size=batch_size, drop_last=False)
for index in sampler:
    print('Batch index: ', index)
    print('Batch data: ', x[index])