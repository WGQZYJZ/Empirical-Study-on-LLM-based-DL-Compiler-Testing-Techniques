
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 512)
 
    def forward(self, x1, y):
        v1 = self.linear(x1) + other # Add another tensor to the output of the linear transformation
        v3 = torch.relu(v1) # Apply the ReLU activation function to the result 
        return v4


# Initializing and running the model
m  = Model()
x1 = torch.randn(64, 512)
other = x1.clone().detach() * 0.708

m(x1, other)

