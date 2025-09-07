
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, q, k, v):
        scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.dim)
        weights = F.softmax(scores, dim=-1)
        output = torch.matmul(weights, v)
        return output


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.attention = ScaledDotProductAttention(64)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        output = self.attention(q=v1, k=v1, v=v1)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
