
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 12)
        # Initializing the module's weight matrices with random values
        self.linear.weight.data.normal_(std=0.3)
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = v1 + other_tensor
        return v2

# Initializing the model and passing a dummy input to it.
m = Model()
x = torch.randn(4, 5) # Dummy tensor with shape (batch size=4, sequence length=5). 
__output__  = m(x)

