
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc  = torch.nn.Linear(784, 10)
 
    def forward(self, x1):
        v1  = self.fc(x1)
        v2  = F.relu(v1)
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
__input__  = torch.randn(32, 784) # A random input tensor of size (32 x 784), where 32 is the number of batches and 784 is the total number of features in each example in the batch


# Inputs to the model
__input__ = torch.randn(1, 784) # A single input tensor of size (1 x 784) representing a single example in the batch


