
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.randn(2)
        v1_permuted = self._permute(v1)

        return v1_permuted

def _permute(self, v1):
    v3 = torch.nn.functional.linear(
            torch.reshape(torch.transpose(x), (-1, x)), 
            self.linear.weight, self.linear.bias
        )

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(2)
__output__  = m(x1)

