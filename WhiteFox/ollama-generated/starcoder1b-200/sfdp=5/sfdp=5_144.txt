
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        k = self.conv(x1).transpose(-2, -1)  # Compute the dot product of the query and key
        qk = k @ torch.tanh((x1 - k) * 0.5 / math.sqrt(x1.size(-1)))  # Compute the scaled dot product of the query and key (plus an attention mask)
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        v = k @ attn_weight  # Compute the dot product of the attention weights and the value
        return v


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
