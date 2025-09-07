
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2): 
        v1 = torch.mm(input1, input2)
        return v1 + input


# Initializing the model
m  = Model()
 
# Inputs to the model
a  = torch.randn(50, 37689) # Size of tensor is (batch_size x 100) in this case batch size equals 'b'.  
b  = torch.randn(42253, 25) # Size of tensor is (1 x 100) in this case batch size equals 'a'
 
# Generating input tensors 
c  = m(a , b)
__output__  = c

