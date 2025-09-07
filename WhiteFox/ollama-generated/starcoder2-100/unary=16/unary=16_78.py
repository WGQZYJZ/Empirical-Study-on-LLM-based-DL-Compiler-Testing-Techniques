
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1024 * 7 * 7, 5)

    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.relu(v1) 
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
__input_tensor__  = torch.randn(8, 5)
x1  = torch.rand(1024 * 7 * 7, 8).requires_grad_(True) # This line is important! Without it, you may get an error when generating the inputs to your model

# Initializing a function from which we want to generate inputs and targets (labels of the target tensor), by first generating an input variable for which we don't have any knowledge about its shape or dimensions. 
f_init = lambda: torch.rand(1024 * 7 * 7, 8).requires_grad_(True) # This line is important! Without it, you may get an error when generating the inputs to your model

