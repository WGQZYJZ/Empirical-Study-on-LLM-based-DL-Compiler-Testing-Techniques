
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
 
        input3  = torch.randn(240, 80) # Initialize the input tensor for the 1st matrix multiplication
        input4  = torch.randn(240, 560) # Initialize the input tensor for the second matrix multiplication
        t1  = torch.mm(x1, input3)   # Matrix multiplication between x1 and input3
        t2  = torch.mm(input4, input3) # Matrix multiplication between input4 and input3
        t3  = t1 + t2 # Addition of the results of the two matrix multiplications
 
        return t3


# Initializing the model