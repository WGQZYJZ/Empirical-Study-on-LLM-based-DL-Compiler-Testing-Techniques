
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, x3):
        v1  = self.conv(x1)  # [B,C,H,W] * [B,C,H',W'] => [B,C,H+H',W+W']
        v2 = v1  * 0.5 
        v3 = v1  * 0.7071067811865476
        v4 = torch.erf(v3)  # [B,C,H,W] * [B,C,H',W'] => [B,C,H+H',W+W']
        v5 = v4  + 1
        v6 = x2 * v5  # [B,C,H,W] * [B,C,H',W'] => [B,C,H+H',W+W']
        return v6


# Initializing the model
m = Model()

