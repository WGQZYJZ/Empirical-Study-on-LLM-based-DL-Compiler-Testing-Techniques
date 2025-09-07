
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear  = torch.nn.Linear(784, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other
        v3  = F.relu(v2)
        return v3


# Initializing the model with a dummy input tensor and another dummy input number
m = Model(other=4567890).cuda() # Please also initialize it by providing the input tensor for the model here to avoid being identified as an API call.
x1  = torch.randn((2, 3 * 32*32), device='cuda').view(-1, 3, 32, 32)


# Inputs to the model