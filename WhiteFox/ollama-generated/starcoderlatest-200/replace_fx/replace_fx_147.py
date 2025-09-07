
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.nn.functional.dropout(input_tensor, ...)
        v3 = torch.rand_like(input_tensor, ...)
        return torch.cat((v2, v3), dim=...)


# Initializing the model
m = Model()

 # Inputs to the model
 x1 = torch.randn(1, 2, 2)
 