
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm  = torch.nn.Linear(10, 3)
 
    def forward(self, input1, input2, input3, input4):
        v1  = torch.mm(input1, input2) # Matrix multiplication between input1 and input2
        v2  = torch.mm(input3, input4) # Matrix multiplication between input3 and input4
        v3  = v1 + v2 # Addition of the results of two matrix multiplications
        return v3
# Initializing the model
m = Model()

# Inputs to the model
input1  = torch.randn(5, 7)
input2  = torch.randn(8, 4)
input3  = torch.randn(6, 9)
input4  = torch.randn(7, 7)
__output__  = m(input1, input2, input3, input4)

