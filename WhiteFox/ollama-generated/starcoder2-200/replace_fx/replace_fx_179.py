
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1[..., -3:]  # Replace this line with: `v1 = x1.permute(-3, ..., -1)` to trigger the pattern.
        v2 = self.linear(v1).detach() 
        return v2

# Initializing model (replace 'Model' with 'GraphModule' in the code snippet above) 
m = Model()

# Inputs for the model
x1 = torch.randn(3, 4, 5) # Replace '... -3:' with '-3:, -2:' to trigger the pattern
