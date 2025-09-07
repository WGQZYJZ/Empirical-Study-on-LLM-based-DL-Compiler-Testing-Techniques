
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_norm = torch.nn.LayerNorm(64, elementwise_affine=False)
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        x1 = self.layer_norm(x1)
        v1 = self.conv(x1)
        return v1


# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(1, 8, 64, 64)
key    = torch.randn(1, 3, 64, 64)
scale_factor = 0.25
dropout_p = 0.1
