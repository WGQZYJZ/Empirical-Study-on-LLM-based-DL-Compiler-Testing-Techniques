
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other
        return v2


# Initializing the model with "other" tensor as "t1" variable and a value 0.5 to be used for addition operation
m  = Model(t1=torch.randn(3,8))

 # Inputs to the model - a random tensor of size (batch_size x channels x width x height) that is not used by the model 
 __input__   = torch.rand(256, 4096, 14, 14)


# Inspect the input of the initial model, "m" using ModelInspector:

from inspector import inspect_model
inspected_model = inspect_model(m)

inspected_model.inputs

outputs = m(**{i: input for i in inspected_model.inputs})

# Inspecting the output of the initial model, "m" using ModelInspector:
from inspector import inspect_model
inspected_model = inspect_model(m)
print('Model input:', inspected_model.inputs)
outputs  = m(**{i: input for i in inspected_model.inputs})

for key in outputs:
    print(key, "Shape:", outputs[key].shape)
