
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0 = torch.zeros((3, 2), device='cuda') # Initialize the tensor on the GPU
        v1 = self._forward(v0)                  # Call a private method
        return v1

    def _forward(self, x1):                   ## Permute the input tensor
        v1 = x1.permute([0, 2, 1])             # Permuting the input
        v3 = torch.nn.functional.linear(v1, self._linear_weight(), bias=None)
                                            ## Linear transformation
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn((5, 20)).cuda()          # Generate input tensor of 5 samples with 20 features each for GPU computing
__output__  = m(x1)                         # Call the model

