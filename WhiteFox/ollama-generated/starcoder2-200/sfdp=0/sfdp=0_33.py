
# Initializing the model
m  = ScaledDotProductAttention()
 
# Inputs to the model
query   = torch.randn(3, 4096, 256//8) # (batch size x seq len x hidden dim)
key     = torch.randn(3, 4096, 256//8) 
value    = torch.randn(3, 4096, 256//8) 

__output__, __attention_weights__  = m(query, key, value, inv_scale=1.0)
