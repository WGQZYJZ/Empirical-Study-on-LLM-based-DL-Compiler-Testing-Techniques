
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v1 * 0.7071067811865476
        v4  = torch.erf(v3)
        v5  = v4 + 1
        v6  = v2 * v5 
        return v6

 # Initializing the model
 m = Model()
 
 # Inputs to the model
 x1 = torch.randn(1, 3, 70, 80)
 
  # The shape of x1 should be (batch size=1, channel=3, 70, 80). 
  # If you cannot find a valid input that matches this requirement, 
  # please refer to the [data type and dimension](https://github.com/pytorch/pythia/tree/master#data-type-and-dimension) section in the `README`.
 
 # Run an analysis
 p1 = Analysis(m, 'model_input')
 
# Check the output of p1
p1()
