
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 - other_tensor 
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
input_shape1  = (3, 64 ,64 ) # Tensor shape of input tensor that will be given for this model.
input_tensor1  = torch.randn(size=input_shape1)


# Running the model and inspecting its outputs
output1  = m(input_tensor1)

