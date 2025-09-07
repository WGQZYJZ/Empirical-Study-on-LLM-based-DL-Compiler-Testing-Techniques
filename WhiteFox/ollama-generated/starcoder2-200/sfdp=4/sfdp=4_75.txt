
import torch
class MLP(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 4)
        self.activation = torch.nn.ReLU()
 
    def forward(self, x):
        return self.activation(self.linear1(x))

mlp = MLP()
inputs = torch.randn(20, 3) # 20 samples with 3 features each
outputs = mlp(inputs)

