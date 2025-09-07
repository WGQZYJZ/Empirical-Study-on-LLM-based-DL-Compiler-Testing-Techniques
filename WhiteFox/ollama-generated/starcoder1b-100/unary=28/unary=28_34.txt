
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=10):
        super().__init__()
        self.linear = torch.nn.Linear(8 * 7 * 7, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1.clamp_(min=self.min_value)
        v3 = v2.clamp_(max=self.max_value)
        return v3


# Initializing the model
m  = Model(min_value=0, max_value=10)


