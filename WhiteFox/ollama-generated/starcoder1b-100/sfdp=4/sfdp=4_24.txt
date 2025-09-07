
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        k = x2 @ x1.transpose(-2, -1) / math.sqrt(x2.size(-1))  # Compute the dot product of the query and key, and scale it
        k = k + attn_mask  # Add the attention mask to the scaled dot product
        qk = torch.softmax(k, dim=-1)  # Apply softmax to the result
        return qk @ v6  # Multiply the value by the result


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
