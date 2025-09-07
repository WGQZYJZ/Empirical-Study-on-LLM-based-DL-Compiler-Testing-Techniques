
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2  = torch.sigmoid(v1)
        return v2

 # Initializing the model
 
m = Model()
 
 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64) 
 
__output__  = m(x1)
 
 # In case of multiple output:

__output__(0)  # To get first output tensor

 __output__(1)  # To get second output tensor

__output__(2)  # to get the third output tensor

__output__(n-3)  # To get the  (n-3)-th output Tensor

__output__(n-1)  # To get last output Tensor

