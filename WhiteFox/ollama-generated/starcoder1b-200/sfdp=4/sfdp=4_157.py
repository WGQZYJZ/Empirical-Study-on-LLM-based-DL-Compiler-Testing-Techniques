
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, x3):
        v1 = self.conv(x1) * x2 + x3
        return v1


# Initializing the model
m = Model()

# Inputs to the model
inputs  = torch.randn(1, 500, 3, 8)
mask_id = torch.tensor([[0, 2], [3, 6]], dtype=torch.long)
mask_pos = torch.tensor([[True, False, True], [False, False, False]], dtype=torch.bool)

# Forward pass to compute the model's outputs
m(inputs, mask_id, mask_pos)


