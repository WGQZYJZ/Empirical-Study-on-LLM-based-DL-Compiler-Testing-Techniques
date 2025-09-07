
class Model(torch.nn.Module):
    def __init__(self, x_dtype, y_dtype):
        super().__init__()
 
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        # self.convert_element_type()
 
    def forward(self, x1):
        t1 = torch.full([x1.shape[0], 1], 1, dtype=x_dtype, layout=x1.layout, device=x1.device, pin_memory=False) 
        # v1 = self.conv(x1)
        v2 = t1 * 0.5  # Multiply the output of the convolution by 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6

# Initializing the model
m = Model(x_dtype=torch.float, y_dtype=torch.half)

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64).to(device)
