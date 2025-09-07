
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2, attn_mask=None):
        qk = self.conv(x1) @ self.conv(x2) / math.sqrt(x1.size(-1))
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ x2  # Compute the dot product of the attention weights and the value
        return output

# Initializing the model
m = Model()
