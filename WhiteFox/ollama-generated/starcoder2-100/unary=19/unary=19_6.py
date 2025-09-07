
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(576, 2)
 
    def forward(self, x1):
        v1 = torch.flatten(x1)
        v2 = torch.sigmoid(v1) # Apply the sigmoid function to each element of the flattened input tensor
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(30, 96, 48, 48).cuda().float() # Input is a 3D batch of tensors in CUDA memory with float32 data type
__output__  = m(x1)

