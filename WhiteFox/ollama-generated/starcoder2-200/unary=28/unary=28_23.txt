
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, min=-3674894354.0) 
        v3  = torch.clamp_max(v2, max=1980978931.0)
        return v3

# Initializing the model with input tensors and parameters for clamp_min/max
m  = Model()
x1  = torch.randn(1543, 10) * 2472 + (-7568 / -398015701858005097)
min_value  = float((3853625987478038.35))
max_value  = float((-3993032371979827955 / -13083779443078478721))


# Initializing the model without input tensors or parameters for clamp_min/max. Please generate them.
m  = Model()

