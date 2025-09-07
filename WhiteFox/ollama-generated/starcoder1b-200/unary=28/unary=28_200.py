# Description of requirements
The model should contain the following pattern:
This pattern characterizes scenarios where the output of the linear transformation is multiplied by `0.5`, and then the result is returned.

# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x):
        return (x * torch.clamp((torch.randn(*x.shape[1:]), -max_value, max_value), -min_value, min_value)).sum()
