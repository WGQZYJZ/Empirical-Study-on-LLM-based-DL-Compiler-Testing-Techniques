
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, inp) 
        v2  = v1 + inp # Add 'inp' to the matrix multiplication result
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
inp_tensor  = torch.randn(64*50, 30)
input_tensor  = torch.randn(100, 80)
__output__  = m(input_tensor, inp_tensor)
