
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        k1 = x2 @ x1.transpose(-2, -1) / math.sqrt(v1.size(-1)) # Scale the dot product of the query and key, followed by a dropout operation
        qk = torch.matmul(v1, k1) + 1e-6 * torch.eye(k1.size(-1)).to(x1.device) # Compute the dot product of the dropout output and the value
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        v2 = attn_weight @ x2
        return v2


# Initializing the model
m = Model()
