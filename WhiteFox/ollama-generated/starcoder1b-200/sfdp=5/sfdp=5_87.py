
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, key, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        attn_mask = torch.zeros_like(qk)
        # Add the attention mask to the scaled dot product
        attn_weight  = torch.softmax(qk, dim=-1) 
        # Apply softmax to the result
        # Apply dropout to the softmax output
        attn_weight = torch.dropout(attn_weight, dropout_p, True) 
        output = attn_weight @ value 
        return output


# Initializing the model
m = Model()


