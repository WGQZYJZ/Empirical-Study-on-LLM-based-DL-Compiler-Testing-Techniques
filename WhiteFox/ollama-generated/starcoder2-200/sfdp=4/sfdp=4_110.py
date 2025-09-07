
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Parameter(torch.rand((10, 8)))
        self.key   = torch.nn.Parameter(torch.rand((32, 64, 8))) 
        self.value = torch.nn.Parameter(torch.rand((32, 64, 64)))

    def forward(self):
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key tensors, scale it by sqrt(dim)
        qk += attn_mask                                            # Add the attention mask to the scaled dot product
        
        # Apply softmax to the result
        attn_weight  = torch.softmax(qk, dim=-1)   
        output       = attn_weight @ value                     # Compute the weighted sum of the query and key tensors
        return v6
 
# Initializing the model
m = Model()
 
