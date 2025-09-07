
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = torch.full([64, 51], 1, dtype=torch.float32, layout="HW", device=device_target("cpu"), pin_memory=False).cumsum(-1) # Create a tensor filled with the scalar value 1, with the specified dtype and layout
        v2 = torch.convert_element_type(v1, torch.float64) 
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 57, 57)
