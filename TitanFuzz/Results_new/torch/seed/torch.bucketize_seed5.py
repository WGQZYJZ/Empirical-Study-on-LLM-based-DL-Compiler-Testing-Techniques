input = torch.arange(0, 10, 0.1)
boundaries = torch.tensor([0, 5, 9])
out = torch.bucketize(input, boundaries, out_int32=True, right=False)
out = torch.bucketize(input, boundaries, out_int32=True, right=True)