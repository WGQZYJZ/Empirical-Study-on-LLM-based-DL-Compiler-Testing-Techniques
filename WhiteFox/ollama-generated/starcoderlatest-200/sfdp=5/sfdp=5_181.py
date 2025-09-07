
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_conv = torch.nn.Conv2d(16, 8, 3, stride=1, padding=1)
        self.key_conv   = torch.nn.Conv2d(16, 8, 3, stride=1, padding=1)
 
    def forward(self, x):
        k = self.query_conv(x) @ self.key_conv(x).transpose(-2, -1) / math.sqrt(k.size(-1)) # Compute the dot product of the query and key
        k  = k + torch.arange(0, k.size(-2)).view(k.size()[:2] + (-1,)) * 1e30  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(k, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        v = attn_weight @ self.value_conv(x).transpose(-2, -1) # Compute the dot product of the dropout output and the value
        return v
