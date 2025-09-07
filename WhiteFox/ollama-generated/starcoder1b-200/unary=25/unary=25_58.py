
class Model(torch.nn.Module):
    def __init__(self, negative_slope: float = 0.25):
        super().__init__()
        self.linear = torch.nn.Linear(3, 16)
        self.negative_slope = negative_slope
 
    def forward(self, x: TensorType[D]) -> TensorType[D]:
        v1 = self.linear(x)
        v2 = (v1 > 0).float() * self.negative_slope
        v3 = torch.where(v2, v1, v2)
        return v3


# Initializing the model
m = Model(negative_slope=0.75)


