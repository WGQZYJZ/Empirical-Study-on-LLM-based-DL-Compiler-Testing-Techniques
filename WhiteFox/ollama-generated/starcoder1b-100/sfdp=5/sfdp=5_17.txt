
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.attn  = torch.nn.MultiheadAttention(key_dim=8, dropout=0.05, num_heads=8)
        self.fc   = torch.nn.Linear(8 * 4 * 4, 2)

    def forward(self, x1):
        q1 = torch.randn(1, 3, 64, 64) / math.sqrt(x1.size(-1))
        k1 = torch.randn(1, 8, 64, 64) / math.sqrt(x1.size(-1))
        v1 = torch.randn(1, 8, 64, 64) / math.sqrt(x1.size(-1))

        # The query and key should be the same, which is why they are multiplied
        k2  = self.attn(q1, k1, value=v1)[0] * 0.5
        k3  = self.attn(q1, k1, value=v1)[0] * 0.7071067811865476
        k2k3 = torch.mul(k2, k3)

        # The output is computed as a scaled dot product between the dropout output and the value
        o  = torch.dropout(torch.matmul(self.conv(x1), k2k3), dropout_p, True)
        output = self.fc(o)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
