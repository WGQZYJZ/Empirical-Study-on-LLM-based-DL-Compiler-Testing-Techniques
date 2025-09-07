
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        qk   = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) + attn_mask
        attn = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn = torch.dropout(attn, dropout_p, True)  # Apply dropout to the softmax output
        v = attn @ value # Compute the dot product of the dropout output and the value
        return v


# Initializing the model
m = Model()


