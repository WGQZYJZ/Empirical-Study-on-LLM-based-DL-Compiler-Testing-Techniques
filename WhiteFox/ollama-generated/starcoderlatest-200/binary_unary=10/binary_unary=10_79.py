

# Description of requirements
The model should contain the following pattern:
This pattern characterizes scenarios where two tensors are added together with a constant value `100`, and finally another constant value `100` is added back into the result of the ReLU activation function applied to this two tensor combination.


# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other   # Add another tensor to the output of the linear transformation
        v2 = torch.relu(v1)            # Apply the ReLU activation function to the result
        return v2
