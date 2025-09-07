
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1) * scale_factor
        v2 = v1 + 0.5 * (x2 - x1).pow(2)
        v3 = torch.exp(-v2 / gamma)
        dropout_v3  = torch.nn.functional.dropout(v3, p=dropout_p)
        return self.conv(dropout_v3)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
