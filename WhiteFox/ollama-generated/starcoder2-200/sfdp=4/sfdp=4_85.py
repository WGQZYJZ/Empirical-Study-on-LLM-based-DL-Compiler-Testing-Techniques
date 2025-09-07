
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout  = torch.nn.Dropout(0.1)
 
    def forward(self, query, key, value, attn_mask):
        attention  = (query @ key.transpose(-2, -1)) / math.sqrt(query.size(-1)) # Scaled dot product
        attention  += attn_mask # Add the mask to scaled dot product
        attention  = torch.softmax(attention, dim=-1) 
        attention  = self.dropout(attention) 
        output      = attention @ value 
        return output


# Initializing the model
m2 = ScaledDotProductAttention()

# Inputs to the model