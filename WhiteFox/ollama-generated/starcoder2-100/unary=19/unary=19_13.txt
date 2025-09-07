
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(256, 8)
 
    def forward(self, x1):
        v1 = self.lin(x1)
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5, 3784) # This is a 5 by 3784 tensor representing 5 images with each image being 3784 pixels in total

