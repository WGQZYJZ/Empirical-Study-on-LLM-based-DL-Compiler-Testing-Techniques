
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1):
         v  = torch.nn.functional.conv3d(input1)
         v2  = torch.nn.functional.batchnorm3d(v)
         return v


# Initializing the model
m  = Model()

 # Inputs to the model.
x1 = torch.randn(1, 10, 8, 5, 7)

