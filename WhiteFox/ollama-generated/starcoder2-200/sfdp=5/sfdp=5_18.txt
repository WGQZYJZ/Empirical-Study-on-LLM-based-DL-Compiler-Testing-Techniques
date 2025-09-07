
class Model(torch.nn.Module):
    def __init__(self, embed = 32, heads = 8):
        super().__init__()
        self.attn_mask = torch.triu(torch.ones((embed//heads, embed//heads), dtype=torch.bool, device="cuda:0") == True)
        self.query  = torch.nn.Linear(in_features=32*32*16, out_features=embed)
        self.key   = torch.nn.Linear(in_features=32*32*16, out_features=embed)
        self.value = torch.nn.Linear(in_features=32*32*16, out_features=embed)
 
    def forward(self, x):
        query  = self.query(x)  # Apply the linear layer to the input tensor
        key   = self.key(x)    # Apply the linear layer to the input tensor
        value = self.value(x)  # Apply the linear layer to the input tensor
        
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))  # Compute the dot product of the query and key, and scale it
        qk  = qk + self.attn_mask                                      # Add the attention mask to the scaled dot product

        attn_weight    = torch.softmax(qk, dim=-1)            # Apply softmax to the result
        attn_weight   /= (1-self.attn_mask).float().sqrt()     # Apply dropout to the softmax output
        output         =  attn_weight @ value                 # Compute the dot product of these attention weights and the value
        
        return output

# Initializing the model
m  = Model(embed=32)

