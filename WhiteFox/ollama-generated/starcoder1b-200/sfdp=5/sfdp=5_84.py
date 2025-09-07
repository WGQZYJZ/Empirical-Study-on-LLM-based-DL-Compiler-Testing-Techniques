
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt((x1.size(-1))**0.5 * (x2.size(-1))**0.5)  # Compute the dot product of the query and key
        qk = qk + torch.zeros_like(qk)  # Add an attention mask to compute scaled dot product
        attn_weight = F.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = F.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        return torch.matmul(attn_weight, x2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 32, 32)
