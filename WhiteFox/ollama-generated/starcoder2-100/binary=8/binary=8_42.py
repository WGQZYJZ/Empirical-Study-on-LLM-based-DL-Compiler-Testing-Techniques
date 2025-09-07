
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
 
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + kwargs['other']
        return v1

# Initializing the model with a tensor to add as the "other" argument when calling `forward` method of Model class instance 
m = Model(other=torch.zeros(4))

 # Inputs to the model, and the "other" argument that is used in `forward` method 
 x1 = torch.randn(1, 3, 64, 64)
 