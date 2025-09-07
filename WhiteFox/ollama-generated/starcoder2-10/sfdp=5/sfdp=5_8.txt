
class Model(torch.nn.Module):
    def __init__(self, dropout_p=0.1):
        super().__init__()
 
        self.query = torch.nn.Parameter(torch.randn(32, 768))
        self.key = torch.nn.Parameter(torch.randn(32, 768))
        self.value = torch.nn.Parameter(torch.randn(32, 1024))
 
    def forward(self, attn_mask=None):
 
        v1  = torch.einsum("ijk->ikj", [self.query])  # Compute the dot product of the query and key
        v2  = torch.einsum("ijk->ikj", [self.key]).transpose(-2, -1)
        v3  = v1 @ v2 / math.sqrt(v1.size(-1)) + attn_mask
 
        v4  = torch.softmax(v3, dim=-1)  # Apply softmax to the result
        v5  = torch.dropout(v4, dropout_p=0.1, training=True)  # Apply dropout to the softmax output
        v6  = v5 @ self.value
 
        return v6

# Initializing the model
m  = Model()


x1  = torch.randn(32, 768).to("cuda")
__output__  = m(attn_mask=None)

# Description of requirements