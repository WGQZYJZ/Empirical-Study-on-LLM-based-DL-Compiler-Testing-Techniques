
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1) - other
        return v1


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3)
  __output__  = m(x1)
  # Outputs from the model
  outputs  = [output for _, output in __output__.named_tensors()]
  # The second output is the desired one
print(outputs[0])

