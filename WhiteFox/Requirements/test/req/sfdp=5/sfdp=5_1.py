# Step 1: Scaled Dot-Product Attention
score = (query @ key.transpose(-2, -1)) / math.sqrt(query.size(-1)) # Compute scaled dot-product attention scores

# Step 2: Additive Masking
score_masked = score + attn_mask # Add attention mask to the scores

# Step 3: Softmax Activation
attn_weight = torch.softmax(score_masked, dim=-1) # Apply softmax along the last dimension

# Step 4: Dropout Regularization
attn_weight = torch.dropout(attn_weight, dropout_p, is_training=True) # Apply dropout to attention weights if in training mode

# Step 5: Weighted Aggregation
output = attn_weight @ value # Multiply attention weights with the value tensor for weighted aggregation
