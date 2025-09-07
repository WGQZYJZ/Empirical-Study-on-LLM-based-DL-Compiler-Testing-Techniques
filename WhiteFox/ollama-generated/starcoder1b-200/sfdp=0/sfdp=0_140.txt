
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1  * 0.5
        v3 = v1  * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6

    def generate_attention_weights(self, query, key):
        v = self.conv(query).float() / math.sqrt(query.size(2))  # Scale to range [0, sqrt(n)]
        w = torch.matmul(v, key) / math.sqrt(key.size(1))
        return w

    def forward_with_attention(self, x1):
        v1 = self.conv(x1).float() / math.sqrt(x1.size(2))  # Scale to range [0, sqrt(n)]
        query = torch.matmul(v1, x1) / math.sqrt(x1.size(1))
        w = self.generate_attention_weights(query, v1).float()
        output = w.matmul(v1) + v1 * w.sum(-2)  # The weighted sum of the value and attention weights
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
