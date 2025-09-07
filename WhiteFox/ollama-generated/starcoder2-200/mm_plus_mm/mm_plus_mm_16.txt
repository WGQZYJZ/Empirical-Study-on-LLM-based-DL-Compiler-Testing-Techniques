
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):  # Inputs x1, x2 of size (800,)
        v1 = torch.mm(x1, x2) 
        return v1


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(800).reshape((10, 80)) # Shape (batch_size = 10, num_inputs = 800)  
