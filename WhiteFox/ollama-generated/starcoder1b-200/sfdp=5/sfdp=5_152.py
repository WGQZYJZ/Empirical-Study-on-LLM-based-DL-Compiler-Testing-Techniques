
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        qk = (x1 @ x1.transpose(-2, -1)) / math.sqrt(x1.size(-1)) # Compute the dot product of the query and key, and scale it
        qk += self.conv.weight * 0.0001  # Add some constant
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        value = self.conv.weight @ x1 # Compute the dot product of the dropout output and the value
        return attn_weight @ value


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
