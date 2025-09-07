
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear()
 
    def forward(self, x1):
        v1  = self.linear(x)
        v2  = torch.clamp_min(v1, min_value=0.)
        v3  = torch.clamp_max(v2, max_value=9.)
        return v3

# Initializing the model<|end_of_model|>
m = Model()

# Inputs to the model<|end_of_inputs|>
input_tensor  = 10 * torch.rand((1, 5))

__output__  = m(x)

