
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v3 = torch.cumsum(x1, 1)
        return v3


# Initializing the model<|end_of_code|>m = Model()

 # Inputs to the model
x1  = torch.rand(4, 20)
__output__  = m(x1)<|end_of_output|>
