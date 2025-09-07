
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_layer = torch.nn.MultiheadAttention()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5

        qk = x1 @ x2.transpose(-2, -1) / (x1.size(-1)**0.5)
        attn_weight = self.attn_layer(qk, query=v6, key=v6, value=v6, mask=v5).transpose(-2, -1)  # Compute the dot product of the dropout output and the value

        output = attn_weight @ x2
        return output


# Initializing the model
m = Model()


