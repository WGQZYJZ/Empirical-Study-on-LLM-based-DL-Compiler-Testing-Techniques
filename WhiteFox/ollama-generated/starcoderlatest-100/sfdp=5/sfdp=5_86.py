
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 768) # Query
        self.key   = torch.nn.Linear(768, 768) # Key
        self.value = torch.nn.Linear(768, 768) # Value
        self.attn  = torch.nn.MultiheadAttention()
 
    def forward(self, x1, x2):
        qk = torch.einsum("b h i d, b h j d -> bi h j", x1, x2) # Compute the dot product of the query and key, and scale it
        qk += attn_mask # Add the attention mask to the scaled dot product
        _, _, h  = self.attn(x1, qk, qk) # Apply multihead attention
        output = torch.einsum("bi h j, bi h d -> b h i d", h, x2) # Compute the dot product of the dropout output and the value
        return output
