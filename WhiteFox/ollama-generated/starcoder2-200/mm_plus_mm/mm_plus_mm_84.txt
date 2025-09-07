
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul1 = torch.mm
        self.matmul2 = torch.mm
 
    def forward(self, input1, input2, input3, input4):
        v1  = self.matmul1(input1, input2) # Matrix multiplication between input1 and input2 
        v2  = self.matmul2(input3, input4) # Matrix multiplication between input3 and input4 
        v3  = v1 + v2 # Addition of the results of the two matrix multiplications
        return v3

# Initializing the model
m = Model()

# Inputs to the model
input1 = torch.randn(8, 5)
input2 = torch.randn(5, 4)
input3 = torch.randn(7, 9)
input4 = torch.randn(9, 6)
