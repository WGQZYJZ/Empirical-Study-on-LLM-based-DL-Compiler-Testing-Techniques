
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        # Compute the Scaled Dot-Product Attention weights for `query`, `key`, and `value`.
        v1  = self.conv(x1)
        v2  = torch.matmul(v1, x2.transpose(-2, -1)) / 0.7071067811865476
        w3  = torch.nn.Softmax(dim=-1)(w2)
        v3  = v2 * w3
 
        # Multiply `value` by the attention weights.
        output = v3.matmul(x2)
        return output


# Initializing the model
m  = Model()


