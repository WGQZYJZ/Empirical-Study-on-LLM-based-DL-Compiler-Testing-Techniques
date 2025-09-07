
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(32 * 64 * 64, 10)
 
    def forward(self, x):
        v1 = F.relu(x.view(-1, 32*64*64)) # Apply the ReLU activation function to the flattened input tensor
        return self.fc(v1)


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(50, 1, 32, 64, 64)
__output__  = m(x)

# 