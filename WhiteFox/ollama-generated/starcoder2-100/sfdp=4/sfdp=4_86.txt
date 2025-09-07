
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, attn_mask=None, value=None):
        v1  = torch.bmm(query, key.transpose(-2, -1)) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        if attn_mask is not None:
            v1 += attn_mask
        v2 = F.softmax(v1)
        output  = torch.bmm(v2, value)
        return output

# Initializing the model
m = Model()

 # Inputs to the model
q = torch.randn(4096, 35, 768)
k = torch.randn(128, 35, 768)
attn_mask  = None
 
