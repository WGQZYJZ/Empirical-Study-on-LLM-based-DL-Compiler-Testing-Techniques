input = torch.tensor([(- 1.1), (- 0.5), 0.5, 1.1])
boundaries = torch.tensor([(- 1), 0, 1])
bucket_indices = torch.bucketize(input, boundaries, right=True)
(unique_indices, unique_counts) = torch.unique(bucket_indices, return_counts=True)