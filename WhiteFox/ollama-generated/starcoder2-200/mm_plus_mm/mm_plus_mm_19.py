
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2, input3, input4):
        t1 = torch.mm(input1, input2)
        t2 = torch.mm(input3, input4)
        t3  =t1 + t2 
        return t3


# Initializing the model with valid inputs and expected output
m = Model()
input1 = torch.randn(50, 100, dtype=torch.float32) # Random matrix of size [50x100] for input1 
input2 = torch.randn(100, 64,dtype=torch.float32) # Random matrix of size [100x64] for input2 
input3 = torch.randn(10, 50 , dtype=torch.float32)# Random matrix of size [10x50] for input3 
input4 = torch.randn(64, 78,dtype=torch.float32) # Random matrix of size [64x78] for input4  
