output_tensor = input_tensor * scalar  # Element-wise multiplication with constant scalar on the input tensor
return output_tensor
output_tensor = input_tensor + scalar  # Element-wise addition with constant scalar on the input tensor
return output_tensor
output_tensor = torch.sin(input_tensor) * scalar  # Element-wise multiplication with constant scalar on the output of the sin operation on the input tensor
return output_tensor
output_tensor = torch.cos(input_tensor) * scalar  # Element-wise multiplication with constant scalar on the output of the cos operation on the input tensor
return output_tensor
output_tensor = torch.tan(input_tensor) * scalar  # Element-wise multiplication with constant scalar on the output of the tan operation on the input tensor
return output_tensor
output_tensor = torch.pow(input_tensor, scalar)  # Element-wise power operation on the input tensor and a constant scalar value
return output_tensor
output_tensor = torch.pow(input_tensor, -1)  # Element-wise negative logarithm operation on the input tensor
return output_tensor
