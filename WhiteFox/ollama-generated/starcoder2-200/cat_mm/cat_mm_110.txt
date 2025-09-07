
class Model(torch.nn.Module):
    def __init__(self, input1=None, input2=None):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)

        # This line is added by you in your task
        v4  = torch.cat([v1] * len(input2), dim=-3)
        
        return v4


# Initializing the model
m  = Model(input1, input2)

# Inputs to the model
x1 = torch.randn(10, 56, 57, 89).requires_grad_(True).to('cuda')

