
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 3)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = v1 - other_value
        v4  = relu(v2)
        return v4

# Initializing the model
m  = Model()
other_value = random.randint(0,9) # Generate a value between 0 and 8

