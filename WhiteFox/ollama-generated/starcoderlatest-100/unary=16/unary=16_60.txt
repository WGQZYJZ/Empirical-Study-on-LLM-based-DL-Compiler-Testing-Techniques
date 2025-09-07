
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28, 10)
 
    def forward(self, x1):
        v1 = x1.view(-1, 28 * 28) # View the input tensor into a tensor with shape (batch_size, -1) which can be used for linear transformation
        v2 = self.linear(v1)
        v3 = torch.nn.functional.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 28, 28)
