
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1, inv_scale=None):
        x = torch.matmul(q1, k1.transpose(-2, -1)) / (inv_scale if inv_scale else 0)
        attention_weights = torch.softmax(x, dim=-1)
        output = attention_weights.matmul(v1)
        return output


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.attention_layer = ScaledDotProductAttention()
 
    def forward(self, x1):
        v1 = self.conv(x1)
        output = self.attention_layer(q1=v1, k1=v1, v1=v1, inv_scale=32.0)
        return output

# Initializing the model
m = Model()


