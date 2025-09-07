
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        qk = x1 @ x2.transpose(-2, -1) / math.sqrt(x1.size(-1))  # Compute the dot product of the query and key, and scale it
        qk = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        qk = torch.dropout(qk, dropout_p, True)  # Apply dropout to the softmax output
        attn_weight = x1 @ x2  # Compute the dot product of the dropout output and the value
        attn_weight = torch.softmax(attn_weight, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        output = qk @ x2  # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 50, 50)
