
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = torch.cat([x1[:, 0:9223372036854775807], x2[:, 0:size]], dim=1) # Concatenate the tensors along dimension 1
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
