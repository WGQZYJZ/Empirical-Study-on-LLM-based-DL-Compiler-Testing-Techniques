
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1, input2) # Perform matrix multiplication on two input tensors 'inp' and 'input2'. 
        v2  = t1 + self.input_tensor # Add the result of the matrix multiplication to another tensor 'input_tensor', which is a public tensor in this example.
        return v2
# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(3, 4)
inp = torch.randn(4, 5) # 'inp' as keyword argument for the forward function of the model.
 
__output__  = m(x1, inp=inp)

