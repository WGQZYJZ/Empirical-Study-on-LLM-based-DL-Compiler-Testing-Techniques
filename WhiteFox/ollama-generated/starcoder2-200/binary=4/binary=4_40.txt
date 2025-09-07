
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3072, 4)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other_tensor
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(64, 3072) # A 5-D array (the batch size is assumed equal to one here.) The size of each dimension is 3072 for the input tensor and 4 for the output tensor.
__output__  = m(x1)

