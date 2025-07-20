input_tensors = []
for i in range(3):
    input_tensors.append(torch.randn(2, 2))
output_tensor = torch.hstack(input_tensors)