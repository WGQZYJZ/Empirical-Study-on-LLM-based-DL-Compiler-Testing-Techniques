
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.relu(x1) # Apply the ReLU activation function to input tensor.
        return v2

# Initializing model
m  = Model()
