
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=0)
 
    def forward(self, x):
        v1  = self.conv(x) 
        v2  = torch.sigmoid(v1) # sigmoid 
        v3  = v1 * v2   # conv*sigmoid
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x_sig = torch.randn(1, 3, 64, 64)

# Initializing the second model and running it on inputs with same size as first model output. It will be possible because the initializers used by default are not shared across runs of a single model instance.

# Generating new model
m2 = Model()
__output_m1  = m(x) # Run 1st model
__output_m2  = m2(x) # Run 2nd model (first model input, input to 2nd model should have the same size as first model output)


