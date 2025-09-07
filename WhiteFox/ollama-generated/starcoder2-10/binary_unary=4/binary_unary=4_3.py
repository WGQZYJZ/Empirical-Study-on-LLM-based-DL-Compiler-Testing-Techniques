
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = self.linear(x1) # Linear transformation applied to the input tensor
        v3  = relu(v2 + other) # ReLU is then applied to add another tensor 
        return v3

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
 
