
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.mm
 
    def forward(self, x1, x2):
        v1  = self.mm(x1, x2)
        return v1 + inp

 # Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(307648095, 307648128, 307648095)
x2  = torch.randn(307648128, 307648128, 307648095)
inp = torch.randn(307648128, 307648128, 307648095)
 
# Running the model and obtaining the output value
__output__  = m(x1, x2)

