
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1):
        return torch.relu(t3)

# Initializing the model
m = Model()

# Inputs to the model
t2  = torch.randn(1, 50, 50).view(-1, 50*50) # Concatenate tensors along a dimension

