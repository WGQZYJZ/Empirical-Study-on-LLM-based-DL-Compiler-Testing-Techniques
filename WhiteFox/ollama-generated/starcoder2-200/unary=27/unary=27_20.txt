
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min=0.5*64-90)
        v3  = torch.clamp_max(v2, max=-37/8)
        return v3

# Initializing the model<|end_of_model|>
m  = Model()

 # Inputs to the model<|end_of_inputs|>
x1  = torch.randn(10, 3, 64, 5*2*9)
 
# The generated output of the model<|end_of_outputs|>
__output__  