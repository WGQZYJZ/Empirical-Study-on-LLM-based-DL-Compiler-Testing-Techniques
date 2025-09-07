
class Model(torch.nn.Module):
    def __init__(self, hidden_size: int = None):
        super().__init__()
        self.linear = torch.nn.Linear(input_dim=1024, hidden_size=hidden_size)
 
    def forward(self, x1):
        v1 = self.linear(x1) + 5  # Add some constant to the output of the linear transformation
        return v1


# Initializing the model
m = Model()


