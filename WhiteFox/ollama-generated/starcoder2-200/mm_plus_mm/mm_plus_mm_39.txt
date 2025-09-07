
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        
        # This line is the only difference between Model() above (in which we multiply input tensors by 0.5) and this Model()
        y1 = torch.mm(x1, x1.transpose(-2,-1)) 

        return y1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 4) # Matrix input tensor of shape (3, 4)


# Run the model with the inputs and check that it returns the right value
y2 = m(x1)

