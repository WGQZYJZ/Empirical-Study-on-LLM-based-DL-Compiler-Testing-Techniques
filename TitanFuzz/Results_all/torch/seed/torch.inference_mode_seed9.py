input_data = torch.randn(1, 1, 28, 28, requires_grad=True)
with torch.inference_mode():
    output = torch.nn.functional.relu(input_data)