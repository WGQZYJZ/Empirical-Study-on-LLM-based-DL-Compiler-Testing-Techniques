
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(256, 3)
 
    def forward(self, x1):
        v1  = self.fc(x1) # Linear transformation applied to the input tensor
        v2  = F.relu(v1) # ReLU activation function applied to the output of linear transformation
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(3, 4096) # Input tensor with shape [3, 4096]
