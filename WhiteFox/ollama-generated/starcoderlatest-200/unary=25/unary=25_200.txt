
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.linear = torch.nn.Linear(3, 16)
        self.negative_slope = torch.nn.Parameter(torch.tensor([negative_slope]))
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 > 0
        v3 = v1 * self.negative_slope
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model and the random number generator
m = Model()
generator = torch.Generator(device="cuda") # The device argument is used to indicate where a tensor will be created on.
generator.manual_seed(0)


# Generating input tensors for the newly generated model
x1 = torch.randn(1, 3, 64, 64, generator=generator)
