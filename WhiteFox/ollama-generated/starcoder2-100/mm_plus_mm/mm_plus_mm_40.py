
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, input1, input2, input3, input4):
        v0  = torch.mm(input1, input2) # Matrix multiplication between input1 and input2
        v1  = torch.mm(input3, input4) # Matrix multiplication between input3 and input4
        v2  = v0 + v1                   # Addition of the results of the two matrix multiplications
        return v2

# Initializing the model
m = Model()

# Inputs to the model
v0_data  = torch.randn(5, 6)
v1_data  = torch.randn(6, 7)
v3_data  = torch.randn(4, 8)
v4_data  = torch.randn(8, 9)
__output__  = m(v0_data, v1_data, v3_data, v4_data)

