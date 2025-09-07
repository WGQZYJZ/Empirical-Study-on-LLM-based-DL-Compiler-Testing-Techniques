
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
       v1 = self.conv(x1)
       return torch.tanh(v1)

# Initializing the model
m  = Model()

 # Inputs to the model
__input_1__, __input_2__  = torch.randn(1,3,64,64), torch.randn(1,3,64,64)
 
# Saving inputs in dictionaries for testing
inputs = {
    '__input_1__': __input_1__,
    '__input_2__': __input_2__}

# Run model under test with the input dictionary 
torch.__output_1__, torch.__output_2__ = m(**inputs)

 # Generate and save a new model to disk by calling the generatedModel
__output__  = generatedModel(inputs, torch.__output_1__)

