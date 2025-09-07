
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = torch.full([x1, x2], 1, dtype=torch.int64, layout=torch.Strided, device=None, pin_memory=False)
        v2 = convert_element_type(v1, torch.float32)
        v3 = torch.cumsum(v2, 1)
        return v3
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randint(0, 4, (1,))
x2 = torch.randint(0, 6, (2,))
