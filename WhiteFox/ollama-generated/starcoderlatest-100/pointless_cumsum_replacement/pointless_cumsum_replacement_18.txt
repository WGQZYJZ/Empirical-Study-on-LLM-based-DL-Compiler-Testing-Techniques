
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = torch.full([x1], 1, dtype=torch.float64, layout=torch.strided, device=torch.device("cpu"), pin_memory=True)
        t1 = convert_element_type(v1, torch.float32)
        v2 = torch.cumsum(t1, 1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randint(0, 5, (1,)).item() # x2 is an integer input. Convert it into a float tensor and use it in the forward method of Model().
