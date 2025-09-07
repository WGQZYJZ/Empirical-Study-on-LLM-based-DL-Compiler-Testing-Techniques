
class Model(torch.nn.Module):
    def __init__(self, input1Size, input2Size, input3Size, input4Size):
        super().__init__()
 
        self.mm0 = torch.nn.Linear(input1Size, 5)
        self.mm1 = torch.nn.Linear(input2Size, 9)
        self.mm2 = torch.nn.Linear(input3Size, 7)
        self.mm3 = torch.nn.Linear(input4Size, 8)
 
    def forward(self, x):
        v0_in = (x[:, :input1Size], x[:, input1Size:]) 
        v0 = self.mm0(*v0_in)
 
        v1_in = (x[:, -input2Size:], ) 
        v1 = self.mm1(*v1_in) 
 
        v2_in = (self._mm(x, 3), x[:5], ) # mm1
        v2 = self.mm2(*v2_in)
 
        v3_in = (self._mm(input4Size, x), ) 
        v3 = self.mm3(*v3_in) 
 
        return torch.cat([v0, v1, v2, v3], 0)

def _mm(x1, y):
    return torch.mm(x1, y)

 # Initializing the model
m = Model(7, 5, 8, 9)
 
# Inputs to the model: 4 tensors, each of size [2 x 3]
input_tensor1  = torch.randn(2, 3)
input_tensor2  = torch.randn(2, 5)
input_tensor3  = torch.randn(7, 8)
input_tensor4  = torch.randn(9, 6)
 
__output__  = m(torch.cat([input_tensor1, input_tensor2], -1)) # Size [10 x 5]
__output__  = m(torch.cat([input_tensor3, input_tensor4], -1)) # Size [8 x 9]

