
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(256*84, 10)
 
    def forward(self, x):
        v1  = self.lin(x)
        v3  = F.relu(v1) # ReLU activation function (Rectified Linear Unit), a common activation function in neural networks.
        return v3
 
# Initializing the model
m  = Model()


# Inputs to the model