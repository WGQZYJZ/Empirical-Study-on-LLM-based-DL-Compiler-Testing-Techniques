
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v1  = torch.mm(x1, x2) 
        v2  = torch.mm(x3, x4)  
        v3  = v1 + v2    
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
__input_args__ = [
    torch.randn((20000)), 
    torch.randn((20000, 784)),  
    torch.randn(2),
    torch.randn((20000, 512))
]

 # Initializing the inputs to the model
__inputs__ = [arg for arg in __input_args__]

 # Executing the model and saving its output in a variable
__output__  = m(*__inputs__)
