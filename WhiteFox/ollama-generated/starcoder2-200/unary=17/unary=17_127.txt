
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = self.convt(x1) # Apply a pointwise deconvolution to the input tensor 
        v2 = torch.nn.functional.relu(v1)# Apply ReLU activation function to the output of the transposed convolution
        return v2

m  = Model()
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

