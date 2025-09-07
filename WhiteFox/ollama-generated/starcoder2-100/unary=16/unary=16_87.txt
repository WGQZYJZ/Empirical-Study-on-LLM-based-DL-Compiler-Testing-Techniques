
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(64*32, 10)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = F.relu(v1) # Apply the ReLU activation function to the output of the linear transformation
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(64, 3*32) # Random input tensor with shape [batch_size, number_of_channels * number_of_rows]
