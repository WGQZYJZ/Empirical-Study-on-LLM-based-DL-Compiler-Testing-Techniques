

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input_tensor):
        v = torch.nn.functional.linear(input_tensor)  # Apply linear transformation to the input tensor
        return conv3d(v, torch.nn.ConvXd(1, 2), torch.nn.BatchNormXd())

m  = Model()


# Initializing the model
x  = torch.randn(10, 5, 64)
__output__  = m(x)

__result__ = [
    "conv3d = torch.ops._torch_python.ops.Conv3d", 
    "linear   = torch.ops._torch_python.nn.Linear"
    ]