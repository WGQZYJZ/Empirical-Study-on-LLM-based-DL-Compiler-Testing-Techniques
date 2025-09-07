
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1=None, inp2=None):
        t1 = torch.mm(inp1, inp2) # Perform matrix multiplication on two input tensors
        t3 = torch.add(t1, 4)
        return t1

# Initializing the model
m  = Model()

 # Inputs to the model 
 inp1  = torch.randn(5, 786)
 inp2  = torch.randn(9087, 73)
 
 # The result from the forward pass of the model is a Tensor (matrix) with dimensions (9087x73)
 result_1 = m(inp1, inp2)

