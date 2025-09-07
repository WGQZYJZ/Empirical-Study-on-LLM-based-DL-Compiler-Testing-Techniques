

class Model(torch.nn.Module):
    def __init__(self, input1=None):
        super().__init__()
        self.input2 = torch.nn.Parameter(torch.rand((8, 5)))
        self.input3 = torch.nn.Parameter(torch.rand((7, 4)))
        self.input4 = torch.nn.Parameter(torch.rand((7, 10)))
 
    def forward(self, x):
        v1  = torch.mm(x, self.input2) # Matrix multiplication between input and input2
        v3  = torch.mm(v1, self.input4) 
        v5  = v3 + v1                   

        return v5

# Initializing the model
m = Model()


# Inputs to the model
input1  = torch.randn((7, 8))
input2  = m.input2.data
input3  = m.input3.data
input4  = m.input4.data
 
 # This part is added for testing purposes only
if input1 != None:
    # Inputs to the model - this part is optional and should be removed in actual code
    input_tensor = torch.randn((7,8)) 
    input2_tensor = torch.randn((8, 5))
    input3_tensor = torch.randn((7,4))
    input4_tensor = torch.randn((10, 7))

    # Inputs to the model - should be equal to initial inputs in previous part if they are not overwritten for testing purposes only
    # input_tensor  = input1
    __output__  = m(input1)


