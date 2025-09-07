
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        x1_t0 = x1[:, :, :64] # Slice along dimension 1
        t0_t1 = x1_t0 * 0.5  # Multiply the input tensor along dimension 1 by 0.5
        t0_t2 = t0_t1 * 0.7071067811865476 # Multiply the input tensor along dimension 1 by 0.7071067811865476
        t3_t4 = x1_t0 * 2  # Multiply the input tensor along dimension 1 by 2
        t3_t5 = x1_t0[:, :, :64] # Slice along dimension 1
        t5_t6 = torch.cat([t0_t1, t0_t2], dim=1) * t3_t4 + t0_t3 * t3_t5  # Add the input tensor along dimension 1 and the sliced tensor along dimension 1 and concatenate along dimension 1
        return t5_t6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
