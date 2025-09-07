
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        l1  = torch.nn.functional.linear(x1) # Apply linear transformation to the input tensor
        l2  = (l1 + 3).clamp(min=0, max=6)/6
        return l2


# Initializing model with inputs and running inference on them
m  = Model()
i  = torch.randn([8, 4]) # Inputs to the model
o_m  = m(i)

