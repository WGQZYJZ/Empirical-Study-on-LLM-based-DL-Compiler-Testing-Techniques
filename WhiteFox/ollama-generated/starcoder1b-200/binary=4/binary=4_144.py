
class Model(torch.nn.Module):
    def __init__(self, input_size):
        super().__init__()
        self.linear1 = torch.nn.Linear(input_size, 8)
 
    def forward(self, x1):
        v1 = self.linear1(x1) + x1
        return v1


# Initializing the model
m = Model(32)
x1 = torch.randn(4, 32) # Generate inputs for the model
