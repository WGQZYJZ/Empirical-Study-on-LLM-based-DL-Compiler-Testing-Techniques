input_data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
subset_indices = [0, 2]
subset = torch.utils.data.Subset(input_data, subset_indices)