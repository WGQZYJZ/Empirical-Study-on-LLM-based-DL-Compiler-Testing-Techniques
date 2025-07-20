input_data = torch.rand(1, 1, 3, 3)
with torch.no_grad():
    output_data = torch.relu(input_data)
    print(output_data)