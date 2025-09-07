
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=None):
        v2 = torch.zeros([x1.shape[0], 8]) + other
        v1 = self.conv(x1)
        v3 = v1 + v2
        return v3

# Initializing the model
m = Model()

 # Inputs to the model, both a tensor and another tensor are needed for model execution
  x1= torch.randn(1, 3, 64, 64)
    