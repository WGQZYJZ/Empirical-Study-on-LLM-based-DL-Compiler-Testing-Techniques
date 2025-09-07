
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        # boolean mask that selects only negative values from the convolution output
        t1_mask = v1 < 0

        v2 = torch.zeros(*v1.size())
        # use the boolean mask to replace all negative values in v2 with values that are calculated based on v1 using an equation
        v2[t1_mask] = -v1[t1_mask] * negative_slope
        
        t3 = torch.where(t1_mask, v1, v2)  # Replace elements from v1 with elements from v2 where the mask is True and multiply the result by a negative slope
        return t3

m = Model()


x1 = torch.randn(1, 3, 64, 64)

__output__  = m(x1)
