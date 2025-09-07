
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y2):
        v1 = torch.mm(x1,y2)  # Matrix multiplication between input1 and input2
        v3 = torch.mm(x1,v1)# Matrix multiplication of the result of matrix multiplication operation of x1 with its own output. This is not a pattern. But it contains the above pattern.
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model (x1 and y2 are the input to the model)
 x1,y2= torch.randn(10,5),torch.randn(5,6)
 