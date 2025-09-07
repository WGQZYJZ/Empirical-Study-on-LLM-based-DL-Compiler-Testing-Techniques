
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2) 
        v2  = torch.cat([v1 for i in range(3)], dim=0) # Concatenate the result tensor along dimension 0 three times
        return v2


# Initializing the model
m  = Model() 


# Inputs to the model
__input1__  = torch.randn(4, 5)
__input2__  = torch.randn(4, 3)


