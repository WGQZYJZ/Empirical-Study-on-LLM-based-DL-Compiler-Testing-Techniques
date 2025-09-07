
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = F.relu(v1) # Add the ReLU function here
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

## Output analysis
You have a 1-element tuple named `(__output__)`. Its elements are: `[tensor([-0.9825])]`.
You have a 1-element tuple named `(v2)`. Its elements are: `[tensor([[-0., -0.,  1., ..., -0., -0., -0.],
        [-0., -0.,  1., ..., -0., -0., -0.]], grad_fn=<ReluBackward0>)]`

__output__ is not equal to (v2).