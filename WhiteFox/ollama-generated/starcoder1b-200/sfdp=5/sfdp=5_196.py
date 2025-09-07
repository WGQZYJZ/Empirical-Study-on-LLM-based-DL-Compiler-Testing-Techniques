
class Model(torch.nn.Module):
    def __init__(self, attn_model=None):
        super().__init__()
        self.attn = attn_model

    def forward(self, x1):
        qk  = x1 @ self.attn.query(x1) / math.sqrt(x1.size(-1))
        qk += torch.zeros_like(qk) # Add an attention mask to the scaled dot product
        attn_weight  = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        value = x1 @ self.attn.value(x1)  # Compute the dot product of the dropout output and the value
        return attn_weight * value

# Initializing the model
m = Model(attn=TransformerModel())


