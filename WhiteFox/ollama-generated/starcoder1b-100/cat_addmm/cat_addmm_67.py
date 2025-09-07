
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, mat1):
        v1  = self.m1(x1)
        return v1 * mat1


# Initializing the model
m = Model()

