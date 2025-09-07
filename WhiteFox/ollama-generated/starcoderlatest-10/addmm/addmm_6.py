
class Model(torch.nn.Module):
    def __init__(self, inp: torch.Tensor = None):
        super().__init__()
 
        if inp is not None:
            self.conv1 = nn.Conv2d(3, 8, 1)
            # Use the keyword argument 'inp' to initialize a tensor with the shape of [1, 8, 64, 64]
            self.conv1.weight.data.copy_(inp)
 
        self.conv2 = nn.Conv2d(8, 8, 1)
 
    def forward(self, x):
        v1 = self.conv1(x) if self.conv1 is not None else x
        v2 = F.relu(v1)
        v3 = self.conv2(v2)
 
        return v3
 
 
# Initializing the model and setting the input tensor to be 0 (for simplicity of this example, only two dimension tensors are supported for inputs).
m = Model()
m[0].weight.data = torch.zeros((1,8,64,64))


# Inputs to the model
inp = torch.randn(1, 3, 64, 64)
m[0].weight.data.copy_(inp)
