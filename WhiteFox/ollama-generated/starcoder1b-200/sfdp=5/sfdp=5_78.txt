
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        qk = self.conv(x1).view(-1, x1.size(1), self.heads * self.dim)
        qk = qk / math.sqrt(qk.size(-1))  # Compute the dot product of the query and key, and scale it
        attn_mask = torch.zeros_like(qk).scatter_(1, x1.view(-1), 1) # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        value = self.conv(x1).view(-1, x1.size(1), self.dim)  # Compute the dot product of the dropout output and the value
        output = attn_weight @ value  # Compute the dot product of the dropout output and the value
        return output

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
