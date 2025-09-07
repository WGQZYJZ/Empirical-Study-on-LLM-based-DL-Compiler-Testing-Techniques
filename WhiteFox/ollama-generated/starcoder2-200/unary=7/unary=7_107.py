
class Model(torch.nn.Module):
    def __init__(self, num_inputs=320):
        super().__init__()
        self.linear = torch.nn.Linear(num_inputs + 64, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * clamp(min=0, max=6, l1  +  3) # clamped_output = 6 if (l1  >  6), otherwise = l1  +  3
        v3 = v2 / 6 
        return v3

m = Model()

