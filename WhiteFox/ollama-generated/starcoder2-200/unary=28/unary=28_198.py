
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 1)

    def forward(self, x):

        v0 = self._get_input()

        v1 = self.linear(v0) # Apply a linear transformation to the input tensor

        v2 = v1.clamp(min=-0.437985366) # Clamp the output of the linear transformation to a minimum value
        v3 = v2.clamp(max=0.585333407) # Clamp the output of the previous operation to a maximum value

        return [v1, v2]

    def _get_input(self):
        
        v0  = torch.randn((64,))

        v1 = self._linear(v0)
        v2 = v1 / 5 + 5 * 3
        v3 = self._activation(v2)
        v4 = self._linear(v3).reshape((-1, 8))
        return [v0, v1]

# Initializing the model
m = Model()

 # Inputs to the model 
 input_tensor = torch.randn(5678,)
__output__  = m([input_tensor])

 