
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) * 0.5
        v2 = self.conv(x1) * 0.7071067811865476
        v3 = torch.erf(v2)
        v4 = v3 + 1
        v5 = v1 * v4
        inv_scale = torch.sqrt(v3.shape[0] / self._dim)
        attention_weights = v5 / inv_scale
        output = v5.matmul(self.value)
        return output


# Initializing the model
m = Model()

