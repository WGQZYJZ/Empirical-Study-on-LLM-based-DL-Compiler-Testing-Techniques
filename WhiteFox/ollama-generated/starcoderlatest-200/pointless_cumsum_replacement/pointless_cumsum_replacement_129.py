
class Model(torch.nn.Module):
    def __init__(self, dtype: torch.dtype = None, layout: Union[torch.layout, str] = "C", device: torch.device = 'cpu'):
        super().__init__()
        self.dtype = dtype
        self.layout = layout
        self.device = device
 
    def forward(self):
        v1 = torch.full([64, 8], 0.5, dtype=self.dtype, layout=self.layout, device=self.device)
        v2 = v1 * 0.7071067811865476
        v3 = torch.erf(v2) + 1
        return v3


# Initializing the model
m = Model()

# Inputs to the model
