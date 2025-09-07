
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        attn  = query @ key .transpose(-2, -1) / math.sqrt(query.size(-1)) 
        attn += attn_mask
        attn_weight  = torch.softmax(attn , dim=-1)
        output   = attn_weight @ value
        return output

# Initializing the model
m  = Model()

# Input tensors to the model (make sure they are of the right shape)
query = torch.randn(2,3,512) # Shape [batch_size, seq_length] - input tensor for query
key   = torch.randn(2,3,512) # Shape [batch_size, num_heads, seq_len, head_dim]. This is the key, 
                             # used to compute the attention weights. Note that these dimensions do not match. 
                             # We use a trick here to make it fit into these dimensions.
value = torch.randn(2,3,512) # Shape [batch_size, num_heads, seq_len, head_dim]. This is the value 
                             # that we'll be computing the dot product of with the attention weights for our outputs.

__output__   = m(query , key , value )
