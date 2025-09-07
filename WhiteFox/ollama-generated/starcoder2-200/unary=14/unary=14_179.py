class Model(torch.nn.Module):
    def __init__(self, conv1=True, conv2=False):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v0 = torch.relu(x1) # ReLU activation function for the input tensor
        v1 = self.conv(v0) if conv1 else None
        v2 = v1 + v0 if conv2 else None
        return v2
m  = Model()

# Loading weights into the model (without initialization)
state_dict  = torch.load('weights/pytorch_weights')
m.load_state_dict(state_dict, strict=False)

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)
