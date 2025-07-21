# Perform a linear transformation on the input tensor
t1 = linear(input_tensor) 

# Create a mask where tensor values are greater than zero
mask = t1 > 0 

# Apply the linear transformation to the input and use the mask to select the positive values
positive_part = torch.where(mask, t1, torch.zeros_like(t1))

# Calculate the output for the negative slope part
negative_part = t1 * negative_slope

# Use the mask to apply the PReLU activation function, 
# selecting between the positive part (leave as is) and negative part (scaled by negative_slope)
output = torch.where(mask, positive_part, negative_part)
