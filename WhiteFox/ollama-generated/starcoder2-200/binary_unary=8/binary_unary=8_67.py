
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) + other
        return torch.relu(v1)


# Initializing the model with `other` defined as constant tensor before.
m2  = Model()
m3  = Model2()

# Inputs to the first and second models are the same.
x1   = torch.randn(1, 3, 64, 64)
__output_of_m0__  = m(x1)
other  = torch.tensor([0., 0., 0., 0.], dtype=torch.float32).reshape(1, 1, 1, 1) 

# Inputs to the third model are also the same as those of the first two models. But, `other` is not defined beforehand anymore in the third model.
__output_of_m1__ = m3(x1).data

