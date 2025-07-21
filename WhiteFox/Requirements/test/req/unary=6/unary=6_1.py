# Step 1: Apply pointwise convolution with kernel size 1 to the input tensor
t1 = conv(input_tensor)

# Step 2: Apply pointwise convolution again to potentially another or the same input
t2 = conv(input_tensor)

# Step 3: Add a constant 3 to the output of the second convolution
t3 = t2 + 3

# Step 4: Clamp the result to a minimum of 0
t4 = torch.clamp_min(t3, 0)

# Step 5: Clamp the result to a maximum of 6
t5 = torch.clamp_max(t4, 6)

# Step 6: Multiply the output of the first convolution by the result after clamping
t6 = t1 * t5

# Step 7: Divide the result of the multiplication by a constant 6
t7 = t6 / 6
