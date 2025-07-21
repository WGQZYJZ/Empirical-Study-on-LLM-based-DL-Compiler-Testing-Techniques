# Step 1: Matrix multiplication between `query` and the transpose of `key`
t1 = torch.matmul(query, key.transpose(-2, -1))

# Step 2: Scale the result of the matrix multiplication by dividing with `inv_scale_factor`
t2 = t1.div(inv_scale_factor) 

# Step 3: Apply the softmax function over the last dimension (-1)
t3 = t2.softmax(dim=-1)

# Step 4: Apply dropout to the softmax result with probability `dropout_p`
t4 = torch.nn.functional.dropout(t3, p=dropout_p)

# Step 5: Perform matrix multiplication between the dropout result and `value`
t5 = t4.matmul(value)
