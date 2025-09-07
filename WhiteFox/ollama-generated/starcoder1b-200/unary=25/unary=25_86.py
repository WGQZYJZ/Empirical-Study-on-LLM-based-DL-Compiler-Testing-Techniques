
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        linear = self.linear(x1)
        positive_slope = torch.zeros((1,), device=linear.device)
        positive_slope[0] = - self.negative_slope
        output  = linear * positive_slope + linear
        return output


# Initializing the model
m  = Model()

