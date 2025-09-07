t1 = x1 + x2 + x3  # Concatenate x1, x2 and x3 along the channel axis
t2 = t1 * 0.25   # Scale the summation result by 0.25
t3 = torch.sigmoid(t2)   # Apply sigmoid to the scaled summation result
output = x4 * t3   # Multiply each element of t3 with x4 and then add it to x4
t1 = torch.mean(attn_weight, dim=-1) # Reduce the dimension along the last axis by summing up all elements in that axis
t2  = x4 * t3   # Multiply each element of t3 with x4 and then add it to x4
output = t1 + t2   # Add the results of multiplication and summation above, and then scale them down
t1 = torch.mean(attn_weight, dim=-1) # Reduce the dimension along the last axis by summing up all elements in that axis
output = x4 * t3   # Multiply each element of t3 with x4 and then add it to x4
t1 = torch.mean(attn_weight, dim=-1) # Reduce the dimension along the last axis by summing up all elements in that axis
output = t1 + t2   # Add the results of multiplication and summation above, and then scale them down
