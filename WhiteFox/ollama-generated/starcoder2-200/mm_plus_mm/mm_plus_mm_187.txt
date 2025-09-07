
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm  = torch.nn.MSELoss()
 
    def forward(self, input1, input2):
        v1  = self.mm(input1, input2)
        return v1


# Initializing the model
m  = Model()

 # Inputs to the model
input1   = torch.randn(3, 4096, requires_grad=True) # Matrix multiplication input between two random matrices of size [3 x 4096]
input2   = torch.randn(3, 4096, requires_grad=True)# Matrix multiplication input between two random matrices of size [3 x 4096]
input3   = torch.randn(7, 8, requires_grad=True) # Matrix multiplication input between a randomly generated matrix of size [7 x 8] and another randomly generated matrix of size [7 x 8]
input4  = torch.randn(512, 7, requires_grad=True) # Matrix multiplication input between two random matrices of sizes [512 x 7] and a third randomly generated matrix of size [7 x 7]

 # Running the model
v  = m(input1, input2)
 