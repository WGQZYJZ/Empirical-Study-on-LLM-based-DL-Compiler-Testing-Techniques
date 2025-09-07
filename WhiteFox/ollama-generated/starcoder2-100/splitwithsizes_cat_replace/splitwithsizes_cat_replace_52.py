
import torch  # noqa: F401


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = [x1[i] for i in range(2)] 
        return torch.cat([v1[j] for j in range(len(v1))], dim=3)


# Initializing the model 
m = Model()
 
# Inputs to the model 
x1 = torch.randn(4, 3, 80, 80) 
 
