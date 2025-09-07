
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(28 * 28, 10)
 
    def forward(self, x):
        v1 = self.linear(x) # linear transformation of the input tensor 
        v4 = F.relu(v3 + other)  # ReLU activation function with additional tensor
        return v5


# Initializing the model