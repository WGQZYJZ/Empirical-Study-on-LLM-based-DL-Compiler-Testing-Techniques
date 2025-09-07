
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, value3):
        v4 = query1 @ key2 .transpose(-2, -1) / math.sqrt(query1.size(-1))  # Compute the dot product of the query and key, and scale it
        v5 = v4 + attn_mask  # Add the attention mask to the scaled dot product
        v6  = torch.softmax(v5, dim=-1)   # Apply softmax to the result
        v7  = v6 @ value3
        return v7


# Initializing the model
m  = Model()
 

# Inputs to the model:
query42=  torch.randn(8, 8, 300, 1)
key53 =   torch.randn(8, 8, 196, 1)
value73 =  torch.randn(8, 8, 196, 124)

 # Outputs of the model:
 __output__  = m (query42, key53, value73)