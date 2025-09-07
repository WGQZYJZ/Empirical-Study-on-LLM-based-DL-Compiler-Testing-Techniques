
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.randn(64) # Generates a 1D tensor with size (64,)
        v3 = self.linear(x1).add_(v2) # Applies linear transformation to the input tensor and adds another tensor to the output of the linear transformation
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
 x1= torch.randn(64, 800)
 
__output__  = m(x1)