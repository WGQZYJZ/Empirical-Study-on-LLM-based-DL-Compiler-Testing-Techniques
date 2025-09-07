
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.Linear(x1)
        v2  = v1 + other # Some random constant tensor is added to the result of the linear transformation.
        v3 = nn.functional.relu(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
other = torch.randn(5, 4)
x1  = torch.rand(4096) # The input is a vector of length 4096 (which is an arbitrary integer number).

# Initializing the model using one of the PyTorch models available online
m_pretrained = torchvision.models.__name__(arch="resnet50")
__output__  = m(x1)

