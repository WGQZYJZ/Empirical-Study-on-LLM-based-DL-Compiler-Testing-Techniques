
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(50*50*32, 48)
 
    def forward(self, x1):
        v1  = self.linear1(x1)
        v2 = v1 + other_tensor # Add the 'other' tensor to output of 'self.linear1'
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model