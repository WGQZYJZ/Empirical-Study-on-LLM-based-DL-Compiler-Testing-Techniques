
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, torch.randn((807456,),  requires_grad=True)) 
        v2 = v1 + other
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()
 
 # Inputs to the model
other  = torch.randn(807456,) 
 x1   = torch.randn(1, 3, 64, 64)
 
__output__  = m(x1)

# User: Okay. Thanks for sharing this example. Let's learn PyTorch with this model.

