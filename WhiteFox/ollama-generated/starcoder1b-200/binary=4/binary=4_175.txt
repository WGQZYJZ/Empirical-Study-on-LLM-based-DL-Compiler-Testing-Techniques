
class Model(torch.nn.Module):
    def __init__(self, input_dim=10, num_layers=2, hidden_dim=8):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, kernel_size=1, stride=1, padding=1)
        self.fc   = torch.nn.Linear(input_dim, num_layers*hidden_dim)
 
    def forward(self, x):
        v1  = self.conv(x)
        for i in range(1, self.num_layers + 1):
            v1 = self.fc[i](v1)  # Apply a linear transformation to the output of the convolution
            v2 = torch.exp(-0.5*self.fc[i+1](v1))  # Add an exponential term that multiplies by itself
        return v1


# Initializing the model
m = Model(num_layers=3)

