
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(1024, 10)
 
    def forward(self, query, key, value):
        v1  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it 
        v1 += attn_mask # Add the attention mask to the scaled dot product
        v2  = torch.softmax(v1, dim=-1)# Apply softmax to the result
        v3  = torch.dropout(v2, dropout_p, True)  # Apply dropout to the softmax output
        v4  = v3 @ value # Compute the dot product of the dropout output and the value
        return v4


# Initializing the model
m  = Model()

# Inputs to the model (where mask_val is an integer constant)
query = torch.randn(128, 512).masked_fill_(attn_mask == mask_val , -float('inf')) # The masked values are replaced with float("-inf")
key = torch.randn(1024, 768) # A random matrix of size [1024 x 768] is generated
value = torch.randn(30522, 768) # A random matrix of size [30522 x 768] is generated

