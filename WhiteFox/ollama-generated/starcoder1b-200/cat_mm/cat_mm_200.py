
class Model(torch.nn.Module):
    def __init__(self, in_dim1, in_dim2):
        super().__init__()
        self.conv  = torch.nn.Conv2d(in_dim1, in_dim2, 3, stride=2, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        return v1 * 0.5 + x2


# Initializing the model
m = Model(in_dim1=3, in_dim2=8)


