
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1) * inv_scale_factor
        v2 = torch.matmul(v1, key.transpose(-2, -1))
        v3 = torch.nn.functional.dropout(v2, p=dropout_p)
        v4 = torch.matmul(v3, value.transpose(-2, -1))
        return v4


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
