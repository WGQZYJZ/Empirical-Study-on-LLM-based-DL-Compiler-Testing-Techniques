
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, other=None):
        v1 = self._linear(x1)

        if other is not None:
            return v1 + other
        
        return v1

# Initializing the model 2
m_new = Model2()

# Inputs to the new model that has the first and second arguments as inputs.
__input1__, __input2__ = torch.randn(1, 30), torch.randn(10)

 # Call the forward method of the new model with both arguments specified
__output1__ = m_new(x1=__input1__, other=__input2__)

 