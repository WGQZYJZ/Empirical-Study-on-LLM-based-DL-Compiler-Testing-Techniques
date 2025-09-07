
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(32*64*64, 10)
 
    def forward(self, x1):
 
        v1 = self.linear(x1)
        v2 = v1 + other # other is not a random constant tensor
        v3 = torch.relu(v2)
 
        return v3


# Initializing the model with the above code
m  = Model()


# Inputs to the model (randomly generated tensor of shape [64, 32*64*64])
other = torch.randn(10).view(-1, 32*64*64) # Note that it is a constant tensor in the pattern. Also, it has the same type as the model's input.


