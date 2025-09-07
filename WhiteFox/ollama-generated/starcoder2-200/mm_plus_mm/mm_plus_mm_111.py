
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.mm(x1[0], 32) + torch.mm(x1[1], 64) # Matrix multiplication between x1 and 32
# Matrix multiplication between the output of the previous matrix multiplication by 32 and x1, and then matrix multiplication between x1 and 64
        v2 = torch.mm(v1 + v1 + x1[0] + v1 * 5 + x1[1], 9) # Addition of all the results obtained in the previous step
# Matrix multiplication between x1, 32, and 64 to obtain 7328 and then matrix multiplication with 9
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(10, 5) # Input x1 for the first matrix multiplication
x2  = torch.randn(13, 4) # Input x2 for the first matrix multiplication
x3  = torch.randn(978, 64) # Input x3 for the second matrix multiplication
x4  = torch.randn(500, 5) # Input x4 for the second matrix multiplication

 __output__= m((x1 , x2), (x3, x4)) # Applying the model to both inputs
