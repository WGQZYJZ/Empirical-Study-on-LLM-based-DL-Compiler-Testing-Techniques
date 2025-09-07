
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        clamped_v2 = clamp(min=0, max=6, l1 + 3)
        scaled_clamped_v3 = l2 * clamped_v2
        div_by_six  = (scaled_clamped_v3 / 6).clamp(min=0)
        return div_by_six


# Initializing the model
m = Model()

