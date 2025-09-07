
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):  # This model has two inputs (x1 and x2)
        v0 = torch.full([36597], 1, dtype=torch.float32)
        v1 = convert_element_type(v0, torch.float32)
        v2 = torch.cumsum(v1, 1)
        return v2
 
# Initializing the model
m = Model()


# Inputs to the model