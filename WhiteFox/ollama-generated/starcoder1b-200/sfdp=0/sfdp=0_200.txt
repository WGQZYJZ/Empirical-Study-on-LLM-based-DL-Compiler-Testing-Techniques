
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = (v2 * v5).unsqueeze(-1)
        query  = x1
        key    = x2
        # Do not forget to multiply the query and key by the attention weights, and then apply softmax over the result.
        attention_weights = torch.matmul(query, key.transpose(-2, -1)) / torch.sqrt(torch.dot(key.size()[-2:], query.size()[:-2]))
        return attention_weights.unsqueeze(0).expand(attention_weights.size()[0], -1) * output


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2  = torch.randn(2, 8, 64, 64)
