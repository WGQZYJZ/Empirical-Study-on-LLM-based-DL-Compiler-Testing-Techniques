
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query):
        key = torch.randn((1024, 64), dtype=query.dtype)
        value = torch.randn((1024, 8*8))
        scale_factor = query[:, -1:].sqrt() # Scale the dot product by a factor
        
        v1 = torch.matmul(query, key.transpose(-2, -1)) 
        v2 = v1 * scale_factor
        v3 = v2.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=0.5) # Apply dropout to the softmax output
        