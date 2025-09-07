
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min=-0.5) # -0.5 is used as a minimum value for the example. You need to provide the maximum and minimum values according to your situation.
        v3 = torch.clamp_max(v2, max=0.8) # 0.8 is used as a maximum value for the example. You need to provide the maximum and minimum values according to your situation.
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1, 1) # -0.5 <= input_tensor <= 0.8 (e.g., the range of [-0.9,-0.6] or [0.7,0.3]) for the example
 
