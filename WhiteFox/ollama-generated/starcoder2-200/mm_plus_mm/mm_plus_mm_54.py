
class Model(torch.nn.Module):
    def __init__(self, input1=None, input2=None):
        super().__init__()
        self.linear  = torch.nn.Linear(input1, input2)
 
    def forward(self, x1):
        v1  = torch.mm(x1, [1] * len(x1)) # Matrix multiplication of x1 with a 1D vector of length x1 (all elements equal to 1). This is necessary because the Linear module expects its input tensors to have at least two dimensions 
        v2  = self.linear(v1)
        return v2


# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(10, 4)
__output__  = m(x1)