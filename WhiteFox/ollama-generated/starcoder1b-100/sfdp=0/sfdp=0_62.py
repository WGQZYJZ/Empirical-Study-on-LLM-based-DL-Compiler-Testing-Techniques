
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = self.conv(x2) * 0.5
        v3 = v1 * v2
        inv_scale = (x1.shape[-1] ** (-1 / 2)).sqrt()
        attention_weights = torch.matmul(v3, v2).softmax(dim=-1)
        output = attention_weights.matmul(v1) * inv_scale
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
