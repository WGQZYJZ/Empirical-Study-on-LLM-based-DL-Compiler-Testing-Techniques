
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 3)
 
    def forward(self, q1):
        v1  = self.linear(q1) 
        v2  = v1 * 0.7071067811865476 # Multiply the output of the first linear layer by another constant 0.7071067811865476
        v3  = torch.sigmoid(v2) 
        v4  = self.linear(q1) 
        v5  = v3 + v4 # Add the output of the first linear layer to the second linear layer without multiplying by another constant in the middle
        return v5
 

# Initializing the model
m  = Model()


# Inputs for the model
q1 = torch.randn(2, 5)
