

# Initializing the model
m = m()

# Inputs to the model
x1 = torch.randn(32, 8, 64, 64)
x2 = torch.randn(32, 8, 51200) # For Transformer models, key and value will be of size (batch_size, head_num * head_size). This is the case for transformer-XL, where key/value pairs are generated from the same set of hidden states.
x3 = torch.randn(64, 51200) # For Transformer models, key and value will be of size (batch_size, head_num * head_size). This is the case for transformer-XL, where key/value pairs are generated from the same set of hidden states.
