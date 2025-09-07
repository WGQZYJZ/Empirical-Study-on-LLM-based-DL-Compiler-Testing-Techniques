
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1=None): 
        v1 = torch.mm(input1, input2)
        return v1 + inp
 
 # Inputs to the model
input1  = torch.randn(3,4)
input2  = torch.randn(5,4)
 
# Running the model and extracting the output tensor 
m = Model()
m_output  = m(x=None)

 