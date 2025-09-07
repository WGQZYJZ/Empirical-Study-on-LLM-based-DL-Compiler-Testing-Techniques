

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key1, value1, attn_mask1):
        
        v1 = torch.einsum('ijk,jmn->imn', [query1, key1]) / math.sqrt(query1.size(-1))
        v2  = v1 + attn_mask1
        v3  = torch.softmax(v2, dim=-1)
        v4  = torch.einsum('ijk,km->ijm', [v3, value1])
        return v4

# Initializing the model
m = Model()

# Inputs to the model
query1 = torch.rand((8,7))
key1 = torch.rand(8, 9)
value1 = torch.rand((8,5))
attn_mask1 = (torch.ones((8,6)) * -float('inf')).tril(-1).triu(-2) + query1 @ key1 / math.sqrt(query1.size(-1)) + 0 # Generate an attention mask of the shape (8,7), which contains positive and negative infinity at positions that should not be considered in the softmax operation
