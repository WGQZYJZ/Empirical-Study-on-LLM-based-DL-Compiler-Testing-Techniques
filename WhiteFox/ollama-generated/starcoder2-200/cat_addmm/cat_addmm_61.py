
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
 
        self.fc = torch.nn.Linear(3 * 64**2, out_features)
 
    def forward(self, x1):
        v1  = self.fc(x1.reshape(-1)) # Rearrange the input to a fully connected layer
        v2  = v1 + torch.tensor(0.)  # Add zero to the output of the fully connected layer
        return v2

# Initializing the model
m  = Model(3)


# Inputs to the model
x1 = torch.randn(64, 64).reshape(-1)
