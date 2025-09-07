
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()

    @torch.jit._export.script_module
    class ScriptLinearModule:
        def forward(self, x1, _weight, bias=None):
            t0 = x1.unsqueeze(2).permute(1, 3, 2)  # Permute the input tensor
            t1 = torch.nn.functional.linear(t0, _weight, bias)  # Apply linear transformation to the permuted tensor.
            return t1

    def forward(self):
        v1 = ...  # Get the first input argument 'v1' which is supposed to be of shape (N, 2, 4).
        weight = self.Linear(v1)  # Retrieve the module from the previous step (the script linear module).

        with torch.no_grad():
            v2 = ...  # Calculate a new input argument 'v2' which is supposed to be of shape (N, 4, 8).
            return self._linear(v2, weight)


# Initializing the model
m = Model()


