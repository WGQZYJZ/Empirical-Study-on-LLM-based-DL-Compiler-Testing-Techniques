
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.full = torch.full((5,), 0., device=device)
        self.cumsum = torch.cumsum(self.full, dim=1)

    def forward(self, x2):
        y1 = torch.full((3,), 2, dtype=torch.float32, device=device, layout='cuda')
        t1 = self.full * 0.7
        t2 = convert_element_type(t1, torch.uint8)
        y2 = torch.cumsum(t2, dim=1)
        return y1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 5)
