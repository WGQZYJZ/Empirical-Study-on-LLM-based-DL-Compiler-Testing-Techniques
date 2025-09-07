
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Apply a linear transformation to the input tensor
        v2  = v1 + self._other_tensor   # Add another tensor to the output of the linear transformation
        return v2

# Initializing the model and creating other tensors. 
m = Model()

__input__ = torch.randn(64, 784)
