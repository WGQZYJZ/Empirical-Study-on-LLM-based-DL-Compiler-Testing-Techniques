
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(128 * 64, 3)
 
    def forward(self, x):
        v0  = torch.randn([5]) # Dummy input tensor to make the model work with public APIs
        v1  = self.linear(v0)
        v2  = torch.nn.functional.relu(v1)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x  = torch.randn([5, 128 * 64]) # Dummy input tensor with 5 samples of 1024 numbers for the 1D convolution
__output__  = m(x)


