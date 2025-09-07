
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, **kwargs):
        v1 = self.linear(x1)
        return torch.clamp_min(v1, min_value=kwargs['min_value'])


# Inputs to the model
input_tensor = ... # Please provide a input tensor
