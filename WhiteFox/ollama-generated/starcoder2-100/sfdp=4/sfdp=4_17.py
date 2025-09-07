
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Parameter(data=0.2*torch.randn(4, 3))
        self.key  = torch.nn.Parameter(data=torch.zeros(16, 5, 8))
        self.value  = torch.nn.Parameter(data=0.3*torch.randn(4, 5))
 
    def forward(self, attn_mask):
        v1  = torch.matmul(self.query,  self.key.transpose(-2, -1)) / math.sqrt(self.query.size(-1)) # Compute the dot product of the query and key
        v2  = v1 + attn_mask  # Add the attention mask to the scaled dot product
        v3  = torch.softmax(v2, dim=-1)  # Apply softmax to the result
        v4  = v3 @ self.value  # Compute the dot product of the attention weights and the value
        return v4

# Initializing the model
m  = Model()
 
# Inputs to the model
attn_mask  = torch.randn(1,50) * -7
__output__  = m(attn_mask)

