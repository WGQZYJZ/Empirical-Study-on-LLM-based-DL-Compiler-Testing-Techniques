
class Model(torch.nn.Module):
    def __init__(self, attn_mask=None):
        super().__init__()
        self.query  = torch.randn(32, 512)
        self.key   = torch.randn(6400, 512)
        self.value = torch.randn(6400, 8)
        self.attn_mask = attn_mask if (attn_mask is not None) else torch.empty([])
 
    def forward(self):
        vq = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        vq = vq + attn_mask  # Add the attention mask to the scaled dot product
        av = torch.softmax(vq, dim=-1)  # Apply softmax to the result
        av = torch.dropout(av, 0.5, True)  # Apply dropout to the softmax output
        vo = av @ value  # Compute the dot product of the dropout output and the value 
        return vo


# Initializing the model
m = Model()

attn_mask  = torch.zeros([128], dtype=torch.long, device="cuda:0")
m(attn_mask)

