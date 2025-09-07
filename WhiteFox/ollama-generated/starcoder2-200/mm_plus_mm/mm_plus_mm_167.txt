
class Model(torch.nn.Module):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.linear1 = torch.nn.Linear(*args)  # Create a linear layer with input features equal to the length of args and output features equal to one of the dimensions of kwargs
        self.relu = torch.nn.ReLU()

    def forward(self, x1):
        v0 = self.linear1(x1) 
        v2 = self.relu(v0)
        return v2

# Initializing the model
m  = Model(35, 84)


x1 = torch.randn(7, 35).cuda() # random inputs to the model (for example, two vectors with 35 features each) on GPU device
