
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=1):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)
        self.min_value = min_value
        self.max_value = max_value
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1.clone()
        v2.clamp_(min=self.min_value, max=self.max_value)
        return v2

# Initializing the model
m = Model(0.5, 1000)

