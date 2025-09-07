

class Model2(torch.nn.Module):
    def __init__(self,  n_in=3):
        super().__init__()

        # Initialize the layer
        self.linear = torch.nn.Linear(n_in ,1)

    def forward(self, x1):

        v1  =  self.linear(x1)
        v2 = clamp(min=0, max=6, l1  +  3) 
        return v2 / 6


# Initializing the model with random inputs to check the behavior of SELU function
torch.manual_seed(754989)

input  = torch.randn(2 , 10 ) # generate a 2D tensor (batch size = 3 , input dimensionality =  10  )
model2 = Model2()
