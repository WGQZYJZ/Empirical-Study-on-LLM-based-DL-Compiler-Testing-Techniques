
class Model2(torch.nn.Module):
    def __init__(self, constant):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self._constant = constant
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1 - self._constant


# Initializing the model with constant 0.5:
m2_half = Model2(.5) # m2_half.conv is torch.nn.Conv2d(3, 8, kernel_size=(1, 1), stride=(1, 1))
__output__  = m2_half(x1)


# Initializing the model with constant 0:
m2_zero = Model2(.5 * torch.zeros_like(m(x1))) # m2_zero is torch.nn.Conv2d(3, 8, kernel_size=(1, 1), stride=(1, 1)) and initialized to all zeros
__output__  = m2_zero(x1)


# Initializing the model with constant 5:
m2_five = Model2(.5 * torch.full_like(m(x1), fill_value=5)) # m2_five is torch.nn.Conv2d(3, 8, kernel_size=(1, 1), stride=(1, 1)) and initialized to all zeros
__output__  = m2_five(x1)

