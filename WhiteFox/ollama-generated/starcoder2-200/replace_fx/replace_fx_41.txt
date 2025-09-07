
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         v2 = torch.rand_like(x1) # Apply dropout to the input tensor
         return v2

# Initializing the model 
m  = Model()
