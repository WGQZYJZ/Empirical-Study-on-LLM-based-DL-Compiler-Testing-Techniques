
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @torch.jit.script_method
    def forward(self, x):
        output = torch.nn.functional.batch_norm(
            x, 
            self.conv1, 
            self.bn1, 
            self.running_mean, 
            self.running_var, 
        )
        return output


# Initializing the model
m = Model()
x = torch.randn(1, 2, 3)

# Input to the model
