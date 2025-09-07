
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2):
        v7 = torch.full([80], 1)
        v9 = convert_element_type(v7, x3)
        v15 = torch.cumsum(v9, 0)
        return v15


# Initializing the model