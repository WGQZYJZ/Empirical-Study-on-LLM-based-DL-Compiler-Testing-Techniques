
class Model(torch.nn.Module):
    def __init__(self, dim1, dim2):
        super().__init__()
        self.l1 = torch.nn.Linear(dim1, dim2)
 
    def forward(self, x1):
        v1  = self.l1(x1)
        v2  = v1 * clamp(min=0, max=6, l1+3) 
        v3 = v2 / 6
        return v3

# Initializing the model with 4 input features and an output feature of size 509. The model is defined for a batch of 8 samples. 
m = Model(dim1=4, dim2=509)

# Inputs to the model. The input tensor is expected to be 8 × 4.
x1  = torch.randn(3*736//4, 3*736%4).reshape(-1,4) # x1 = torch.randn(320, 3)
__output__  = m(x1)

