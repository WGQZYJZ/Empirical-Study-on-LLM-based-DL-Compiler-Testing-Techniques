
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         v3 = torch.cumsum(convert_element_type(torch.full([args["arg1"], args["arg2"]], 1), args["dtype"]), dim=0)

# Initializing the model with some args in the initialization stage of the model
m = Model()

 # Inputs to the model
x1  = torch.randn(3, 4)
