
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 196)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = F.relu(v1) # Replace this line with `return v1` if you want to keep the linear layer only.
        return v2


# Initializing the model
m  = Model()


# Inputs to the model