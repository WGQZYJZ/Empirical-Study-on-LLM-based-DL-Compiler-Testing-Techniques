
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, other=None): 
        v2 = self.conv(x1) + other
        return v6

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

other = torch.randn(3)

# Call of the model with the input and keyword argument 'other' as 'other'=other
