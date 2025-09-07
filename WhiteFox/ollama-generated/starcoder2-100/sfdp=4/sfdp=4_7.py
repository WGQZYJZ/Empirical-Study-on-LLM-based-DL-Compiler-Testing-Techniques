
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, value3, attn4, mask5):
        v1  = query1 @ key2.transpose(-2,-1) / math.sqrt(query1.size(-1)) # Compute the dot product of the query and key, and scale it
        v2  = v1 + attn4
        v3  = torch.softmax(v2, dim=-1) # Apply softmax to the result
        v4  = v3 @ value3 # Compute the dot product of the attention weights and the value tensor 
        return v4


# Initializing the model
m  = Model()

# Inputs to the model
v5  = torch.randn(2,80)
v6  = torch.randn(17, 80, 320) # Key with size 320x80
v7  = torch.randn(49, 320)      # Value of the same size as key with the size 320x320
v8  = torch.ones((15, 2)) # Attention mask that has size 15x2
v9  = 0.7 * v6 + v5[:,None,:] # Masked query
__output__  = m(v9, v6, v7, v8, v5)

