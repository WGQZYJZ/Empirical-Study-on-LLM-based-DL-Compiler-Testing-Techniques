
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.3):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 768)
        self.negative_slope  = negative_slope
 
    def forward(self, x):
        v1  = self.linear(x)
        v2  = (v1 > 0).type_as(torch.tensor(1))
        v3  = -self.negative_slope * torch.clamp(-v1, min=0.)
        v4  = v2*v1 + v3*(~v2) # where (~v2) is the logical NOT of v2 and is used to convert a boolean value into an integer that can be added (see https://discuss.pytorch.org/t/how-to-convert-boolean-values-to-ints/71685), then we multiply by the negative slope if the element was True, or 0 otherwise
        return v4

# Initializing the model
m = Model(negative_slope=0.3)


# Inputs to the model
x1 = torch.randn(256, 784).to(torch.device('cuda')) # input tensors of shape (batch size x number of elements in the flattened input tensor) for GPU.
__output__  = m(x1)

