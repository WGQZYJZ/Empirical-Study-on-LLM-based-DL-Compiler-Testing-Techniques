input_data = torch.randn(10, 3, 224, 224)
sampler = torch.utils.data.SequentialSampler(input_data)
for i in range(10):
    index = sampler.__iter__().__next__()
    print(index)