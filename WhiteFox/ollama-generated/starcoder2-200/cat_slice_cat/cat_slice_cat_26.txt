
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, *inputs):
        out = torch.cat(inputs, dim=0)
        return out[:9223372036854775807]

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(5, 1000, 300)
x2  = torch.randn(4, 999, 400)
__output__  = m(x1[7], x2[-1])
