
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) * 0.5
        v2 = v1 * 0.7071067811865476
        v3 = torch.erf(v2) + 1
        qk = v2 @ v3
        attn_weight = torch.softmax(qk, dim=-1) * 0.5
        output = attn_weight @ v1 # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
