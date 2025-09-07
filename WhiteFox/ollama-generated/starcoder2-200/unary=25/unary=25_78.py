
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28, 1)

    def forward(self, x1):
        v1  = self.linear(x1) 
        v3  = torch.where((v1 > 0), v1, (-1 * v1))
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
__input_data___  = torch.randn(4759, 28* 28)
x1  = __input_data___
 
 # Expected outputs of the model
__output_expected___  = m(__input_data__)
