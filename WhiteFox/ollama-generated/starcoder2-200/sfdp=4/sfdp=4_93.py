class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key2, value3, attn_mask=None):
        v1  = query1 @ key2.transpose(-2,-1) / torch.sqrt(query1.size()[-1])  # Compute the dot product of the query and key, and scale it
        v1 += attn_mask  # Add the attention mask to the scaled dot product
        v2  = torch.softmax(v1, dim=-1)  # Apply softmax to the result
        v3  = value3 @ v2 # Compute the dot product of the attention weights and the value
        return v3
v4 = torch.randn(64, 7)
v5 = torch.randn(7, 8)
attn_mask  = torch.tensor([[0., -2147483648.,  1., -2147483648.], [1.,     0., -2147483648., -2147483648.]])
