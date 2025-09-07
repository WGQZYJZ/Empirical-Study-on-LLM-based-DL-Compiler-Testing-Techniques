
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.Linear(8*8*3 , 5)(x1)
        v2 = v1 + other
        return v2

# Initializing the model and specifying the additional tensor that is used in the model pattern (in this case: `other`)
m = Model()
other = torch.randn(8, 8, 3).cuda()


# Inputs to the model
x1 = torch.rand((160, 8*8*3)).cuda() # Input tensor for the linear transformation in the model pattern 
