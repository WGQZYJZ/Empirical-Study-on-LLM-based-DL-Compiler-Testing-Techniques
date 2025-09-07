
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        t = torch.full([4], 1, dtype=torch.float32, layout='cuda', device='cpu')
        t = convert_element_type(t, torch.float32)
        t += torch.cumsum(t, dim=1)
        return t

# Initializing the model
m = Model()


