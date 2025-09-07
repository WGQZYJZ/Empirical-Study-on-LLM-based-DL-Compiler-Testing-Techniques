
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other # add another tensor
        v3  = F.relu(v2) 
        return v3

# Initializing the model with input tensors for both sides of the linear transformation and ReLU activation function
m, other_tensor = Model(), torch.randn(500, 3)
 
# Inputs to the model
x1 = torch.randn(1, 3) + other_tensor # add another tensor
