input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sampler = torch.utils.data.SequentialSampler(input_data)
for i in sampler:
    print(i)