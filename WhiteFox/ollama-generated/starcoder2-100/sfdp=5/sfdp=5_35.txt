
# Initializing the model
m = Model()
 
 # Inputs to the model
 query, key, value, attn_mask  = torch.randn(1, 80, 32)

 # Attention masks
 mask = (torch.arange(query.size(-2))[:, None] > torch.arange(key.size(-2))[None, :])
 
# Mask is 3D; applying the same mask to all attention heads is not necessary. Instead, apply it to one head only.
 mask[attn_mask == False ] = float('-inf')
 
 # Dropout rate of 0.1 for the dropout operation in the model
dropout_p = 0.1
 
# Actual model input and output
x1, x2, x3  = query, key, value  # The input keys do not change
__output__, attn_weight  = m(query)

