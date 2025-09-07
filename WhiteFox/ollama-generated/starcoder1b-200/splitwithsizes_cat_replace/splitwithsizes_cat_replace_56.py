

# Description of requirements
The model should contain the following pattern:
This pattern characterizes scenarios where ReLU operation is applied to the input tensor and then addition and multiplication of the two outputs are performed.


# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1 = torch.relu(x1)  # Apply ReLU to input tensor and store output in variable `t2`

        if self.training:
            t3 = t1 + x2  # Add x2 to the output of Relu
            return t3
