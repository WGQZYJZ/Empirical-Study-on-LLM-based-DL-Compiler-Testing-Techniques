
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3,8, bias=True)
        self.conv  = torch.nn.Conv2d(3, 8, 50, stride=7)
 
    def forward(self, x1):
       l1 = self.linear1(x1)
       l2 = l1 * clamp(min=-64, max=9, l1 + 5*l1) # This is where the new output of the linear transformation would be generated. The original output was used as the new input here for clarity
       l3 = l2 / 8
       return self.conv(x1 * l3)


# Initializing the model
m2  = Model()


