
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.addmm(v1, mat1, mat2) # Applying a matrix multiplication operation and then concatenating the result to the output of the previous convolution layer 
        return  torch.cat([v2], dim=0)

# Initializing the model
m = Model()

