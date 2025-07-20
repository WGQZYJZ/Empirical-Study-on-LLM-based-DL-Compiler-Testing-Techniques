input_data = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=torch.float32)
output_data = torch.square(input_data)
mean_output = torch.mean(output_data)
sum_output = torch.sum(output_data)