

# Initializing the model
m  = Model()

# Inputs to the model
query = torch.randn(64, 768) # query
key   = torch.randn(64, 512) # key
value = torch.randn(64, 1024) # value
attn_mask = torch.ones([64, 30]) > 0 # attention mask

