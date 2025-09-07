
class Model(torch.nn.Module):
    def __init__(self, min_value=0.1, max_value=2.1):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1.clone()
        v2.clamp_(self.min_value, self.max_value)
        return v2


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
