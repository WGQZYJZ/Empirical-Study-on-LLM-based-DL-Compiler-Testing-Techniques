
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 1)
        self.negative_slope = 0.5
 
    def forward(self, x2):
        v1 = self.linear(x2)
        v2 = v1 > 0
        v3 = v1 * -0.749617932080397
	v4 = torch.where(v2, v1, v3)
        return v4

 # Initializing the model
m  = Model()
 
 # Inputs to the model
x2  = torch.randn(1, 8)
 
  # __output__ is expected to be of shape (1 x 8), where each value is less than or equal to zero
__output__  = m(x2)
