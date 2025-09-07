
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other
        return v2


# Initializing the model and providing 'other' as an argument of the class initializer
m = Model(torch.randn(3, 8))


# Inputs to the model for 'other': 
# [Tensor of shape (10,) with the 64 most common English words concatenated and filled by a single element of random float from (-5., -2.) range.]

other = torch.tensor([
	-3,
	9787,
    -3857,
    73733,
    ...
    -10064,
     5932,
     33733]
)

 # Inputs to the model: the 'other' argument of the class initializer should be used as a 4th input tensor to the model. 
 # Input tensor 3 should not be used at all. The order is not important. The inputs to the model can contain random values. 
 x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(30, 578934, dtype=torch.int32)
 
 
 