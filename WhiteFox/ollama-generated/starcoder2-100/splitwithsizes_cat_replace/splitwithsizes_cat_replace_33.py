
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split = torch.nn.Sequential(
            torch.nn.Conv2d(3, 8, kernel_size=5), 
            torch.nn.ReLU(), 
        )
    
    def forward(self, x1):
      v0 = [torch.split(x1, split_sizes=[16], dim=-1)]
      v2 = self.split[0](v0[0][0]) 
      v3 = v2  * 0.5
      return [v0, v2]
# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
__output__  = m(x1)[1] # Please check this line. This line is just to return an output tensor that matches the test framework's expectations. Do not modify this line!

