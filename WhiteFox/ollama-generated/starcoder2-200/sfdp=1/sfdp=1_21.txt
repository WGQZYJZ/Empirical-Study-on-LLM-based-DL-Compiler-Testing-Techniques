
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.matmul(x1, 32)
        v2  = self.conv(v1)


# Initializing the model
m  = Model()


